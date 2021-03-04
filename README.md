# clone-practice

branch practice repo

## How to start practice

1. 클론을 합니다.
2. fizzbuzz.py를 만듭니다.
3. add, commit 합니다.
4. README.md를 업데이트 합니다.
5. fizzbuzz.py를 업데이트 합니다.(print('it works'))
6. 각 작업에 대해 commit을 합니다.(docs, feat)

## What is fizzbuzz?

~while i goes up to 1~100,~

<!-- 
  TODO: fizzbuzz-if min nums of commit: 4 
  브랜치를 만들고 갈아탄 뒤, 일을 하고 브랜치 위에서 push 한 후, main 브랜치에 merge
-->
if i is times of 3: print 'fizz'
if i is times of 5: print 'buzz'
if i is times of 15: print 'fizzbuzz'
else, print i

## fizzbuzz with Korean or uppercase

<!-- main: all strings with Korean -->
<!-- conflict-test: all strings with uppercase -->

<!-- 'fizzbuzz' replaced with Korean, 'buzz' converted to uppercase, leave 'fizz' to lowercase -->

## fizzbuzz with list comprehension

- for conflict test
<!-- Main: range 1 to 300, all string should be lowercase -->
<!-- fb-listcomp: fizzbuzz with list comprehension (range 1 to 100) -->
print(['fizz' if i%3==0 else i for i in range(1,100+1)])

<!-- fizzbuzz with list comprehension (range 1 to 300) -->


## Numguess

- TODO: trial-3

- version: v1.1

- commands

1. git checkout develop

2. git flow feature start ng-trial
3. Add feature: trial
4. git flow feature finish ng-trial

5. git flow release start v1.1
6. git flow release finish v1.1
<!-- after 3 commit -->

7. push to your develop, main, tags




