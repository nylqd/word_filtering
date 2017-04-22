# word_filtering

Word filtering demo implement by dfa and trie in Python

### dfa
example of dfa while word list is `敏感词 用例 test case tea`

```
{
 { 敏 : False
	 { 感 : False
		 { 词 : True
		 }
	 }
 }
 { 用 : False
	 { 例 : True
	 }
 }
 { t : False
	 { e : False
		 { s : False
			 { t : True
			 }
		 }
		 { a : True
		 }
	 }
 }
 { c : False
	 { a : False
		 { s : False
			 { e : True
			 }
		 }
	 }
 }
}
```

### trie
example of dfa while word list is `敏感词 用例 test case tea`

```
{
 { 敏 : None
	 { 感 : None
		 { 词 : 敏感词
		 }
	 }
 }
 { 用 : None
	 { 例 : 用例
	 }
 }
 { t : None
	 { e : None
		 { s : None
			 { t : test
			 }
		 }
		 { a : tea
		 }
	 }
 }
 { c : None
	 { a : None
		 { s : None
			 { e : case
			 }
		 }
	 }
 }
}
```

