#include<iostream>
#include "ray.h"

using namespace std;

vec3 color(ray r){
  float y = unit_vector(r.direction()).y();
  float t = (y + 1.0)/2.0;
  vec3 blue = vec3(0.0, 0.0, 1.0);
  vec3 white = vec3(1.0, 1.0, 1.0);
  return (1 - t)*white + t*blue;  
}

int main(){
  int nx = 200, ny = 100;
  cout << "P3\n" << nx << " " << ny << "\n255\n";
  vec3 lower_left_corner(-2.0, -1.0, -1.0);
  vec3 horizontal(4.0, 0.0, 0.0);
  vec3 vertical(0.0, 2.0, 0.0);
  vec3 origin(0.0, 0.0, 0.0);
  for (int j = ny - 1; j >= 0; j--){
    for (int i = 0; i < nx; i++){
      float u = float(i) / float(nx);
      float v = float(j) / float(ny);
      ray r(origin, lower_left_corner + u * horizontal + v * vertical);
      vec3 col = color(r);
      int ir = int(255.99 * col[0]);
      int ig = int(255.99 * col[1]);
      int ib = int(255.99 * col[2]);
      std::cout << ir << " " << ig << " " << ib << "\n";
    }
  }

  return 0;
}
