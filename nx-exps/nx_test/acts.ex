defmodule F do
  import Nx.Defn

  defn logaddexp(x1, x2) do
    amax = Nx.max(x1, x2)
    delta = Nx.subtract(x1, x2)
    aux = delta |> Nx.abs |> Nx.abs |> Nx.negate |> Nx.exp |> Nx.log1p
    Nx.add(amax, aux)
  end

  defn softmax(t) do
    Nx.exp(t) / Nx.sum(Nx.exp(t))
  end

  defn log_sumexp(x, opts \\ []) do
    opts = keyword!(opts, axis: -1)
    axes = transform(opts[:axis], &List.wrap/1)

    transform({x, axes}, fn {x, axes} ->
      Enum.each(axes, fn axis ->
        Nx.Shape.normalize_axis(Nx.shape(x), axis, Nx.names(x))
      end)
    end)

    max_val = stop_grad(Nx.reduce_max(x, axes: axes, keep_axes: true))

    stable_exp =
      x
      |> Nx.subtract(max_val)
      |> Nx.exp()

   stable_exp |> Nx.sum(axes: axes, keep_axes: true) |> Nx.log
  end
end
