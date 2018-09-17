#include <stdio.h>
#include <stdlib.h>

struct Trie{
  char ending;
  struct Trie *node[26];
};

typedef struct Trie trie;

trie *create(){
  trie *ret = calloc(1, sizeof(trie));
  return ret;
}

void insert(trie *dict, char *word){
  int pos = (word[0] <= 'Z')?(word[0] - 'A'):(word[0] - 'a');
  if((dict->node)[pos] == NULL) (dict->node)[pos] = create();
  if(word[1] == '\0') (dict->node)[pos]->ending = 1;
  else  insert((dict->node)[pos], word + 1);
}

int search(trie *dict, char *word){
  int pos = (word[0] <= 'Z')?(word[0] - 'A'):(word[0] - 'a');
  if((dict->node)[pos] == NULL) return 0;
  if(word[1] == '\0') return (dict->node)[pos]->ending;
  search((dict->node)[pos], word + 1);
}

int main(){
  int n, q;
  trie *dict;
  char aux[15];
  dict = create();
  scanf("%d %d", &n, &q);
  for(int i = 0; i < n; ++i){
    scanf("%s", aux);
    insert(dict, aux);
  }

  for(int i = 0; i < q; ++i){
    scanf("%s", aux);
    printf("%d\n", search(dict, aux));
  }
  return 0;
}
