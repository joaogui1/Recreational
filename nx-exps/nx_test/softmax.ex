defmodule F do
  import Nx.Defn

  defn logaddexp() do
    amax = Nx.max(x1, x2)
    delta = Nx.sub(x1, x2)
    aux = delta |> Nx.abs |> Nx.abs |> Nx.negate |> Nx.exp |> Nx.log1p
    Nx.add(amax, aux)
  end

  defn softmax(t) do
    Nx.exp(t) / Nx.sum(Nx.exp(t))
  end
end
