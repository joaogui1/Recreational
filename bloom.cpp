#include <bits/stdc++.h>

#define ff first
#define ss second

using namespace std;
typedef pair<int, int> pii;

int Hash(pii seeds, int n, int size){
	return (seeds.ff*n + seeds.ss)%size;
}

class bloom_filter{
	int number_hashes;
  bitset <1009> bits;
	vector<pii> hashes_seeds;

	public:
		bloom_filter(int);
  	void add(int x){
			for(int i = 0; i < number_hashes; ++i)
				bits.set(Hash(hashes_seeds[i], x, 1009));
			return;
		}
	  int check(int x){
			for(int i = 0; i < number_hashes; ++i)
				if(!bits[Hash(hashes_seeds[i], x, 1009)])
					return 0;
			return 1;
	  }
};

bloom_filter::bloom_filter(int k){
	int a, b;
	number_hashes = k;
	for(int i = 0; i < k; ++i){
		a = rand()%1009, b = rand()%1009;
		hashes_seeds.push_back(pii(a, b));
	}
}

int main(){
	bloom_filter a (3);
	a.add(5);
	a.add(7);
	printf("%d\n", a.check(8));
}
