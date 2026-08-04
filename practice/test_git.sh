#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)

echo "===== 1. practice-branch 생성 및 이동 (swtich : 이동, -c : create / 브랜치 생성) =====
git switch -c practice

# 브랜치 생성 이전 방식(git branch, checkout)
# $ git branch feature/quiz-ui
# $ git checkout feature/quiz-ui


echo "===== 2. 테스트용 파일 생성 및 커밋 ==="
mkdir -p "$REPO_ROOT/practice
echo "Git branch test contenct" > practice_note.text

# 깃 추가 및 커밋
git add "$REPO_ROOT/practice/practice_note.txt"
git commit -m "test: add practice note in practice folder"


# 만약 팀과 협업중이라면
# $ git push origin [branch명]
# pr 날리고 승인받고 머지될거임
# 그이후에 메인으로 돌아와서 풀당기기 

echo "========= 3. main 브랜치로 복귀 ====="
git switch main

echo "===== 4. practice 브랜치 병합 (merge) ===="
git merge practice

echo "=== 5. 사용 완료된 practice 브랜치 삭제 ==="
git branch -d practice

echo "=== 모든 깃 브랜치 테스트 과정이 프로젝트 루트 기준으로 완벽하게 완료 됌. ==="


# 사용 시
# chomod +x test_git.sh
# ./test_git.sh