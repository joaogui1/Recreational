ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

clean:
> rm ex.ppm
> rm 1

run: clean
> g++ main.cpp -o 1
> ./1 >> ex.ppm
> eog ex.ppm

git:
> @read -p "Message:" msg;
> git add -A
> git commit -m msg

