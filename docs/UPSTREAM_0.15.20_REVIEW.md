# pstack 0.15.20 수동 병합 검토안

> 이 문서는 초기 부분 병합의 기록이다. 이후 전체 최신 동기화 결과는 [UPSTREAM_0.15.24_SYNC.md](UPSTREAM_0.15.24_SYNC.md)를 참고한다.

2026-10-14 KST에 GitHub와 실제 Git checkout을 재확인했다. 이번 구현 범위는 check-plan 파서와 회귀 테스트다. 나머지 변경은 아래의 검토 및 반영 순서 제안이며, 전체 0.15.20 동기화를 완료한 것은 아니다.

## 확인 기준과 제외한 작업

- Codex main: `3fa71cfe09a4dd58b3c58106810c61b7a77295e9`.
- [PR #2](https://github.com/ColdTbrew/pstack-codex/pull/2)는 closed 및 merged. 0.15.17 동기화는 반복하지 않는다.
- [Issue #3](https://github.com/ColdTbrew/pstack-codex/issues/3)는 open, 댓글 0. 저장소 PR 검색 결과는 #2뿐이었다. main의 lock도 0.15.17이므로 0.15.20 전체 반영 완료 증거는 없다.
- 이전 upstream: `11713c683fe4add4fd403ea880580abbc9e0875f`.
- 이번 upstream: `1b6d44ff26d4e242f4e8f68c391e6d2f7ca16def` (0.15.20).
- 이 두 commit의 실제 diff 및 저장소의 stage 도구로 31개 변경 / 자동 후보 20개 / 수동 대상 11개를 재현했다.
- 이후 Codex main의 `4c34459`, `3fa71cf`는 Sol/Luna 라우팅과 Luna fast service tier를 변경했다. 이 변경과 Astra 설정, 현재 TOML 프로필을 보존한다. Terra를 복원하지 않는다.
- `comment_sicko` 프로필과 no-comments의 호출명은 이미 Codex 방식으로 일치한다. upstream 이름 정규화의 효과가 존재하므로 추가 변경하지 않는다.
- Unslop은 이미 보고서 한정 설명이고 명시 호출 정책을 갖는다. upstream의 `Must always apply` 제거는 재적용할 필요 없다.
- 최신 cursor/plugins main은 별도로 `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, pstack **0.15.24**였다. Issue #3의 0.15.20은 최신 전체 버전이 아니다. 요청한 0.15.20 diff를 정확히 고정했고 0.15.21~24를 섞지 않았다. check-plan.mjs에는 0.15.20 이후 추가 변경이 없다. 전체 최신 동기화는 별도 diff 검토가 필요하다.

## 구현한 수정

`plugins/pstack-codex/skills/poteto-mode/scripts/check-plan.mjs`의 코드 블록 순회 부분만 upstream에서 가져왔다.

- 여는 fence는 0~3개의 공백 뒤 동일 문자 3개 이상의 backtick 또는 tilde다.
- 문자 종류와 길이를 기억한다. 닫는 fence는 같은 문자, 여는 것 이상의 길이, 뒤에는 공백/탭만 허용한다.
- 긴 backtick 블록 내부의 짧은 fence, 다른 문자 및 info 문자열이 붙은 줄은 닫힘으로 처리하지 않는다.
- backtick fence의 info 문자열에는 backtick을 허용하지 않는다. tilde info 문자열에는 허용한다.
- code 표시가 heading/checkbox 판별에 전달되므로 예제의 가짜 PR 제목과 checkbox가 실제 검증 구조에 섞이지 않는다.
- Codex LANES, PROGRAM_MARKERS와 파서 뒤의 모든 검증 코드는 baseline과 바이트 단위로 동일함을 확인했다.
- 닫는 fence 줄은 upstream과 동일하게 code=false다. 해당 줄은 제목/checkbox가 아니므로 구조에 영향을 주지 않는다.

`check-plan.test.mjs`는 upstream 5개 테스트 그룹의 fixture를 Codex 규칙으로 전환하고 7개 그룹을 추가했다. 이 환경에 Bun이 없어 Node 내장 test runner를 사용했다. 기존 `bun test orch watch-pr`를 그대로 유지하면서 package.json의 test 앞에 Node 회귀 테스트를 연결했다. 향후 자동 후보인 upstream `check-plan.test.ts`는 그대로 추가하지 말고 이 테스트로 대체해야 한다. 두 파일을 함께 두면 Cursor fixture가 Codex 검증기에 실패한다.

검증 결과:

- 수정 검증기: **12/12 통과**.
- baseline 검증기에 같은 테스트 실행: **5 통과, 7 실패**. 파서 오류가 재현됐다.
- 1/2/3 lane 정상 계획 수용, Cursor `Ten lanes` 및 `/loop 1h` fixture 거부.
- lane 번호, screenshot, pass predicate, unit/live/perf rule과 perf 항목 검증 유지.
- fenced 가짜 heading/checkbox 무시, 코드 뒤 문장부호 진단 및 실제 줄번호 검증.
- EOF까지 열린 fence, 4칸 들여쓰기, 짧은/다른/접미사 포함 닫는 fence 검증.
- Node syntax check, git diff whitespace check, `scripts.sync_upstream.validate_plugin` 통과.
- 기존 orch/watch-pr Bun suite와 typecheck는 이 환경의 Bun 및 설치된 프로젝트 의존성 부재로 실행하지 않았다. 이 파일들은 수정하지 않았다. 전체 회귀를 통과했다고 주장하지 않는다.

실행:

```bash
cd plugins/pstack-codex/skills/poteto-mode/scripts
node --test check-plan.test.mjs
# Bun과 프로젝트 의존성이 준비된 환경에서 전체 suite
npm test
npm run typecheck
```

주의: 현재 검증기는 “up to three”라는 규칙 문구와 연속 lane 번호를 검사하지만 lane 개수 자체를 3 이하로 제한하지 않는다. 이번에는 기존 동작을 보존했고 이 별도 정책 강화는 넣지 않았다. 또한 일반 Markdown 전체 파서가 아니므로 list/blockquote 내부 fence나 4칸 들여쓰기 코드 블록 전체 지원을 주장하지 않는다.

## 수동 병합 대상 11개

경로는 원본 pstack 기준이다. SKILL.md와 playbook은 문서 형식이지만 실행 에이전트의 행동을 지시하므로 동작 변경으로 분류했다.

| 원본 경로 | 성격 | 실제 upstream 변경 | Codex 반영안과 보존 조건 |
| --- | --- | --- | --- |
| `skills/poteto-mode/scripts/check-plan.mjs` | 실행 코드 | fence 종류·길이·들여쓰기·종료 조건 인식 | 이번에 구현·테스트. Codex 검증 상수 및 후속 검증 보존 |
| `skills/poteto-mode/scripts/worktree-audit.sh` | 실행 코드 | `-b/--base`, help, repo/ref 검증, 기본 origin/HEAD→main→master, 명시 refspec fetch, MERGED 기준 ref와 출력 추가 | 해당 기능만 이식. Codex sessions/archived_sessions JSONL 검색, LAST_CHAT, wip/open PR/최근 작업 보류와 삭제 없는 동작 보존. 아래 fixture 검증 후 cleanup 문서와 함께 반영 |
| `skills/create-verification-skill/SKILL.md` | 에이전트 동작 | 빈 데이터 dir에서 migration/seed 완료 후 사용 가능해야 ready. 전제 누락은 실패/ Gotchas. 대체 환경이 숨긴 setup은 미검증 | 해당 문장을 `.agents/skills` 경로를 유지하며 이식. 실패를 피하려 journey를 약화하지 않기. 컨테이너 증거를 실제 VM 증거로 바꾸지 않기 |
| `skills/poteto-mode/SKILL.md` | 에이전트 동작 | 호출받은 chat이 playbook 실행, delegate에게 전체 runner 역할 넘기지 않음 | root가 plan/playbook/spawn을 소유한다는 문장만 추가. 최신 모델 라우팅·작업 소유권·fresh agent 규칙 보존 |
| `agents/poteto-agent.md` | 에이전트 동작/프로필 설명 | full runner에서 delegate 역할로 명확화 | 대응 `codex-agents/poteto_agent.toml` 설명과 instructions에 “delegated slice” 및 root ownership 명시. skill 전체 읽기는 유지. model/reasoning/service tier를 upstream 값으로 덮지 않기 |
| `skills/poteto-mode/playbooks/babysit.md` | 에이전트 동작/보고 | step 6의 중복 merge 금지 경고와 최종 Reply 문단 삭제, step 9의 명시 승인 gate는 유지 | 자동 삭제하지 않기. Codex의 merge/auto-merge 승인 gate, frozen queue, frontier/rearm/stop 조건, 결과 보고 유지. 현재 파일에 step 2~6이 중복되어 있는 별도 문제가 있어 정리는 독립 diff와 watcher 검증 후 수행 |
| `agents/comment-sicko.md` | 설정/식별자 | frontmatter `Comment Sicko`→`comment-sicko` | 이미 `comment_sicko.toml` name과 호출 일치. 추가 수정 제외. 원본 provenance만 전체 동기화 때 갱신 |
| `skills/no-comments/SKILL.md` | 설정/호출 참조 | Task subagent_type 이름 소문자로 정규화 | 이미 read-only `comment_sicko` custom agent 사용. 추가 수정 제외. lint/TS suppression 검사와 accepted finding 처리 보존 |
| `skills/unslop/SKILL.md` | 설명/호출 정책 | description의 `Must always apply` 삭제 | 이미 보고서에만 적용하며 명시 호출. 추가 수정 제외. 적용 범위를 넓히지 않기 |
| `README.md` | 사용자 문서 | root chat runner와 delegate 구분, Comment Sicko 이름 정규화 | Codex README에 동일 ownership 설명 추가. `$pstack-codex:*`와 TOML명 유지, source README는 provenance에 보존 |
| `.cursor-plugin/plugin.json` | 배포 메타데이터 | 0.15.17→0.15.20 버전 | 전체 검토 완료 시 Codex manifest와 CODEX_PORT 및 lock를 함께 갱신. Cursor manifest를 활성 manifest로 복사하지 않기 |

## 권장 반영 순서와 통과 조건

1. **이 patch를 독립적으로 반영.** parser+Codex tests+test command만 반영한다. 이 단계에서는 upstream-lock 및 버전을 0.15.20으로 올리지 않는다.
2. **watch-pr 페이지네이션을 한 묶음으로 반영.** 자동 후보 `github.ts`, `policy.ts`, `types.ts`, 두 test 파일과 `fakes.test-helper.ts`를 같이 이식한다. `reviewThreads()`→`reviewThreadPage()` 계약이 바뀌므로 일부만 반영하면 깨진다. 100개 초과 리뷰 스레드에서 다음 페이지 blocker와 pass count, 기존 READY/WAITING/ADVANCE/COMPLETE를 검증하고 Bun suite 및 typecheck를 통과시킨다.
3. **worktree audit 및 cleanup 문서를 함께 반영.** 아직 -b 없는 script에 새 문서만 먼저 반영하지 않는다. 로컬 bare origin fixture에서 `--help`, 인자 누락/알 수 없는 옵션, 잘못된 repo/ref, origin/HEAD→main→master fallback, integration으로 -b 지정, single-branch clone의 새 remote ref fetch와 fetch 실패 경고를 검증한다. 서로 다른 base에서 MERGED 판정이 달라지는 worktree를 만들고 tracked WIP·open PR·Codex 최근 transcript의 보류 bucket을 확인한다. 어떤 fixture worktree도 삭제되지 않아야 한다.
4. **검증 skill 및 coordinator/delegate 설명을 반영.** create-verification-skill의 readiness/seed/대체 환경 요구와 poteto-mode·poteto_agent·README의 ownership 설명을 묶는다. parent가 plan과 playbook을 소유하고 delegate가 bounded slice만 수행하는 Codex 새 task로 smoke 확인한다. 변경 없는 comment_sicko/no-comments/unslop은 제외한다.
5. **나머지 자동 후보를 검토 후 반영.** “자동 후보”는 이미 승인된 변경을 뜻하지 않는다. Ketchup과 principle/source 문서도 Codex 호출·도구 가용성·근거 요구를 확인한다. 신규 root `plugin.json`은 agent-plugins 메타데이터이며 name/repository가 Cursor pstack을 가리킨다. Codex manifest와 중복되는 활성 등록 파일로 그대로 추가하지 말고 provenance 보존 또는 Codex 전용 정규화 필요성을 먼저 결정한다.
6. **최종 후보 검증 후 lock/version을 원자적으로 갱신.** stage한 정확한 0.15.20 commit을 유지하며 적용한다. `.sync/candidate`의 check-plan에는 이번 patch를 옮기고 upstream `check-plan.test.ts`는 삭제/대체한다. source hashes는 원본 기준으로 보존한다. plugin/skill validators, Cursor 의존성 검사, 전체 tests/typecheck, 설치 및 새 Codex task smoke 후 lock와 plugin을 같은 commit에 넣는다. 현재 더 최신인 main을 대상으로 --stage를 다시 실행하면 0.15.24가 잡히므로 고정 checkout을 `--source`로 사용한다.

[공식 동기화 절차](https://github.com/ColdTbrew/pstack-codex/blob/main/docs/UPSTREAM_SYNC.md)의 --apply-staged는 plugin 전체 교체와 lock 갱신을 하므로 이번 부분 patch만으로 실행하지 않았다. GitHub push, PR 생성, issue 댓글 또는 merge도 수행하지 않았다.
