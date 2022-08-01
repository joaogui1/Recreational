defmodule NxLearning do
  @moduledoc """
  Documentation for `NxLearning`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> NxLearning.hello()
      :world

  """
  def hello do
    t = Nx.tensor([[1, 2], [3, 4]])
    Nx.shape(t)
  end
end
