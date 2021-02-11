### A Pluto.jl notebook ###
# v0.11.13

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
        el
    end
end

# ╔═╡ 74a0d740-f206-11ea-02ff-773958bc4f1d
using PlutoUI

# ╔═╡ 8b13ccca-f15a-11ea-38e7-574502e755a4
begin
	using Images
	philip = load("philip.jpg")
end

# ╔═╡ 39b35d5a-f15a-11ea-0490-357b602c0c6c
# url = "https://i.imgur.com/VGPeJ6s.jpg"

# ╔═╡ 5a3e373c-f15a-11ea-3bae-7305866991b7
# download(url, "philip.jpg")

# ╔═╡ c765e284-f15b-11ea-0796-4f8e8120b763
typeof(philip)

# ╔═╡ 78efef5a-f15d-11ea-2d21-6d469bec1c86
size(philip)

# ╔═╡ e14b055c-f206-11ea-2b48-ffe6f859a991
@bind a Slider(1:1000)

# ╔═╡ 4f7cd6ec-f207-11ea-1bf8-a33e73c28dcd
@bind b Slider(1001:3000)

# ╔═╡ 4fb3a940-f207-11ea-32e8-5fa773ee006c
@bind c Slider(1:1000)

# ╔═╡ 4fe6abec-f207-11ea-18b0-a5329335e75b
@bind d Slider(1001:2988)

# ╔═╡ 95896c2a-f15d-11ea-1c33-eb5e33be21ed
philip[a:b, c:d]

# ╔═╡ c1d90c18-f15d-11ea-2d9d-73dc6d4e089e
begin
	(h, w) = size(philip)
	head = philip[(h ÷ 3): h, (w ÷ 10): (9w ÷ 10)]
end

# ╔═╡ 28c16da8-f15e-11ea-249a-058b5db29fa3
[
	head                  reverse(head, dims=2)
	reverse(head, dims=1) reverse(reverse(head, dims=1), dims=2)
]

# ╔═╡ 4eee07d4-f15e-11ea-0a30-575788892449
begin
	new_dog = copy(philip)
	new_dog[10:20, 1:10] .= RGB(0, 1, 0)
	new_dog
end

# ╔═╡ 3064f872-f15e-11ea-00b3-9f3e5085e4b4
function perm(color)
	return RGB(color.b, color.r, color.g)
end

# ╔═╡ a6e5e432-f160-11ea-11ce-1f2bb611ac82
perm.(philip)

# ╔═╡ af78a6f4-f160-11ea-2d7a-9d27dffba833
p(x) = 3*x + 2

# ╔═╡ 41539042-f208-11ea-3a02-1b20b04cec08
f(x, y) = 2p(x) + y

# ╔═╡ Cell order:
# ╠═74a0d740-f206-11ea-02ff-773958bc4f1d
# ╠═39b35d5a-f15a-11ea-0490-357b602c0c6c
# ╠═5a3e373c-f15a-11ea-3bae-7305866991b7
# ╠═8b13ccca-f15a-11ea-38e7-574502e755a4
# ╠═c765e284-f15b-11ea-0796-4f8e8120b763
# ╠═78efef5a-f15d-11ea-2d21-6d469bec1c86
# ╠═e14b055c-f206-11ea-2b48-ffe6f859a991
# ╠═4f7cd6ec-f207-11ea-1bf8-a33e73c28dcd
# ╠═4fb3a940-f207-11ea-32e8-5fa773ee006c
# ╠═4fe6abec-f207-11ea-18b0-a5329335e75b
# ╠═95896c2a-f15d-11ea-1c33-eb5e33be21ed
# ╠═c1d90c18-f15d-11ea-2d9d-73dc6d4e089e
# ╠═28c16da8-f15e-11ea-249a-058b5db29fa3
# ╠═4eee07d4-f15e-11ea-0a30-575788892449
# ╠═3064f872-f15e-11ea-00b3-9f3e5085e4b4
# ╠═a6e5e432-f160-11ea-11ce-1f2bb611ac82
# ╠═af78a6f4-f160-11ea-2d7a-9d27dffba833
# ╠═41539042-f208-11ea-3a02-1b20b04cec08
