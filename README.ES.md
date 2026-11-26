<div align="center">

# ⚡ OpenCode Olympus Skills

**Flujos independientes e instalables para OpenCode V2 que funcionan sin [OlympusAgents](https://github.com/Edulynch/OpenCode-OlympusAgents).**

🌐 [English](README.md) · [Español](README.ES.md)

[![CI](https://github.com/Edulynch/OpenCode-OlympusSkills/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Edulynch/OpenCode-OlympusSkills/actions/workflows/ci.yml)
[![Licencia MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![OpenCode V2](https://img.shields.io/badge/OpenCode-V2-5964f2?style=flat-square)](https://opencode.ai/docs/)

**[⚡ Instalar](#install) · [🎯 Probar](#try) · [🧩 Skills](#skills) · [⌨️ Atajos](#shortcuts) · [📚 Guías](#guides)**

</div>

## 🚀 Empieza aquí

<a id="install"></a>
### ⚡ Instalar

Instala la skill para redactar goals:

```text
npx skills add Edulynch/OpenCode-OlympusSkills --skill olympus-goal-writer --agent opencode
```

Para instalar todas las skills en OpenCode desde la raíz del proyecto destino:

```text
npx skills add Edulynch/OpenCode-OlympusSkills --skill "*" --agent opencode
```

Los atajos slash de Olympus se instalan por separado; consulta [Atajos](#shortcuts).

<a id="try"></a>
### 🎯 Probar

Después, pídele a OpenCode:

```text
@olympus-goal-writer Convierte lo que acordamos en un goal para OpenCode.
```

La skill redacta una línea `/goal` de hasta 4,000 unidades de código UTF-16; no inicia la tarea. Pega el resultado tú.

## 🧭 Elige un flujo

Escribe `@` seguido del ID de la skill. Los flujos de GitHub requieren una sesión autenticada en [`gh`](https://cli.github.com/); para publicar cambios también se requiere `git`.

<a id="skills"></a>
### 🧩 Skills

| Skill | Para qué sirve | Fuente del atajo opcional |
| --- | --- | --- |
| [`olympus-goal-writer`](.opencode/skills/olympus-goal-writer/SKILL.md) | Redacta un `/goal` de hasta 4,000 unidades de código UTF-16, mantiene el avance independiente cuando algo se bloquea y no lo ejecuta. | [`olympus.goal.write.md`](commands/olympus.goal.write.md) |
| [`olympus-git-issue-list`](.opencode/skills/olympus-git-issue-list/SKILL.md) | Ordena issues abiertos y muestra prioridades, bloqueos y subissues; solo lectura. | [`olympus.git.issue-list.md`](commands/olympus.git.issue-list.md) |
| [`olympus-git-issue-create`](.opencode/skills/olympus-git-issue-create/SKILL.md) | Convierte hallazgos en issues independientes o árboles nativos de epics/subissues; puede mostrar un borrador primero. | [`olympus.git.issue-create.md`](commands/olympus.git.issue-create.md) |
| [`olympus-git-issue-work`](.opencode/skills/olympus-git-issue-work/SKILL.md) | Trabaja issues indicados o elige un grupo priorizado, implementa y prueba, y por defecto deja los PRs abiertos. | [`olympus.git.issue-work.md`](commands/olympus.git.issue-work.md) |
| [`olympus-git-issue-check`](.opencode/skills/olympus-git-issue-check/SKILL.md) | Reporta con evidencia qué pasó, qué falta, las excepciones aceptadas y porcentajes original/actual; solo lectura. | [`olympus.git.issue-check.md`](commands/olympus.git.issue-check.md) |
| [`olympus-git-pr-ready`](.opencode/skills/olympus-git-pr-ready/SKILL.md) | Abre o continúa un PR, espera CI y corrige fallas de la tarea; lo deja abierto salvo que pidas merge. | [`olympus.git.pr-ready.md`](commands/olympus.git.pr-ready.md) |
| [`olympus-skill-author`](.opencode/skills/olympus-skill-author/SKILL.md) | Crea o actualiza una Agent Skill y puede redactar su atajo opcional. | [`olympus.skill-author.md`](commands/olympus.skill-author.md) |

<a id="shortcuts"></a>
### ⌨️ Atajos

El CLI de Skills instala la skill elegida. Los atajos son archivos fuente opcionales: copia solo el `.md` que elijas de [`commands/`](commands/) a `.opencode/commands/` en el proyecto destino. Cada atajo carga su skill correspondiente y reenvía `$ARGUMENTS`; no se instala automáticamente.

## 🧪 Validación local

```text
python -m pip install -r scripts/requirements-ci.txt
python -B scripts/test_validate_frontmatter.py
python -B scripts/validate_frontmatter.py
```

El flujo de GitHub Actions valida el frontmatter y analiza todo el historial Git disponible con la salida de Gitleaks redactada.

## 🤝 Ayuda y políticas

- [Contribuir](CONTRIBUTING.md) · [Reportar un problema de seguridad](SECURITY.md)
- [Abrir un issue no sensible](https://github.com/Edulynch/OpenCode-OlympusSkills/issues) · [Licencia MIT](LICENSE)

<a id="guides"></a>
### 📚 Guías

- [Skills de OpenCode](https://opencode.ai/docs/skills/) · [Comandos de OpenCode](https://opencode.ai/docs/commands/) · [Especificación de Agent Skills](https://agentskills.io/specification)
