# Adaptive Taskcraft

AIエージェントが、タスクの実際のリスクに応じて計画、ツール、テスト、安全性、検証の強度を調整するための移植可能な `SKILL.md` です。

すべての依頼に重い手続きを強制せず、3段階の厳密度と5段階の実行ループを使います。

`ALIGN -> FRAME -> ACT -> PROVE -> DELIVER`

自然な回答、計画、TDD、根本原因のデバッグ、CI修復、フロントエンドとFigmaの実装、ブラウザテスト、CLI・MCP設計、外部サービス連携、脅威モデリング、段階的なツール開示の知見を統合し、再設計しています。

## なぜ必要か

エージェントは、次の両極端で失敗しがちです。

- 手順不足：暗黙の仮定、危険な書き込み、未検証の完了報告
- 手順過多：小さな作業に長い計画、文脈の過負荷、不要なツールの読み込み

Adaptive Taskcraft は、信頼できる証拠を得るために必要な最小のワークフローを選びます。

## インストール

このリポジトリ全体を `adaptive-taskcraft/` としてエージェントのスキルディレクトリに配置してください。`SKILL.md` だけでなく `references/` も保持します。

一般的な配置例：

```text
~/.hermes/skills/adaptive-taskcraft/SKILL.md
~/.agents/skills/adaptive-taskcraft/SKILL.md
<project>/.agents/skills/adaptive-taskcraft/SKILL.md
```

スキルの検出方法はホストごとに異なります。キャッシュされる場合は、インストール後に再起動するか、新しいセッションを開始してください。

まず中核の `SKILL.md` を読み込み、専門領域が必要な場合だけ `references/capability-modules.md` を読みます。

## 言語サポート

英語、中国語、日本語をサポートします。ユーザーが使った言語と丁寧さに合わせ、識別子、コマンド、ログ、エラーメッセージは正確性のため原文を保持します。

## 原則

- 定型句を避け、自然に回答する
- 受け入れ条件を持つ成果ベースの計画
- ツールと専門指示の段階的な読み込み
- 垂直な振る舞い単位と必要量のTDD
- 最小権限、同意、ロールバック、脅威への配慮
- 新しい証拠に基づく完了報告

## 範囲

本リポジトリには、スキル指示、構造テスト、出典、MITライセンスが含まれます。第三者コードや特定プロバイダー向けプラグインは同梱しません。

出典と帰属は [SOURCES.md](SOURCES.md) を参照してください。専門モジュールは [`references/capability-modules.md`](references/capability-modules.md) にあります。

## テスト

```bash
python -m pytest -q
```

## ライセンス

MIT。Copyright 2026 MoonsvnLyn and FirmamentalSpring.
