defmodule AOC2024.Day02 do
  @moduledoc """
  Advent of Code 2024, day 2: Red-Nosed Reports.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(fn line -> line |> String.split(" ") |> Enum.map(&String.to_integer/1) end)
  end

  @doc """
  Solve part 1.
  """
  def part1(data), do: data |> Enum.count(&is_safe/1)

  @doc """
  Solve part 2.
  """
  def part2(data), do: data |> Enum.count(&is_safe_if_dampened/1)

  @doc """
  Check if a report is safe.

    A report consistst of consecutive levels and is safe if:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    ## Examples:

        iex> is_safe([1, 2, 4, 7, 8, 10, 13])
        true
        iex> is_safe([7, 6, 4, 2, 1])
        true
        iex> is_safe([8, 6, 4, 4, 1])
        false
        iex> is_safe([1, 5])
        false
  """
  def is_safe(report) do
    report
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.map(fn [first, second] -> second - first end)
    |> then(fn increases ->
      Enum.all?(increases, fn inc -> 1 <= inc and inc <= 3 end) or
        Enum.all?(increases, fn inc -> -3 <= inc and inc <= -1 end)
    end)
  end

  @doc """
  Check if a report becomes safe if it's dampened.

  Tolerate a single bad level, and count the report as a safe if removing a
  single level makes it safe.

  ## Examples:

      iex> is_safe_if_dampened([8, 6, 4, 4, 1])
      true
      iex> is_safe_if_dampened([1, 5])
      true
      iex> is_safe_if_dampened([9, 7, 6, 2, 1])
      false
  """
  def is_safe_if_dampened(report), do: is_safe_if_dampened(report, [])
  def is_safe_if_dampened([], done), do: is_safe(done)

  def is_safe_if_dampened([current | rest], done) do
    is_safe(Enum.reverse(done, rest)) or is_safe_if_dampened(rest, [current | done])
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
