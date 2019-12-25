ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

all: clean run


run:
> g++ main.cpp -o 1
> ./1 >> ex.ppm
> eog ex.ppm

clean:
> rm -f ex.ppm
> rm -f 1

git:
> @read -p "Message: " msg;
> git add -A
> git commit -m msg

