# OpenCode Olympus Skills

Skills independientes para OpenCode V2, con comandos opcionales. Funcionan sin [OlympusAgents](https://github.com/Edulynch/OpenCode-OlympusAgents) y más adelante podrán ofrecerse como complementos opcionales de la suite.

## Redactar un goal para OpenCode

[`olympus-goal-writer`](.opencode/skills/olympus-goal-writer/SKILL.md) convierte un prompt, un issue o una conversación en una línea `/goal` de hasta 4,000 caracteres, lista para copiar. Le indica al agente que siga con las tareas independientes si un paso se bloquea y que solo pida intervención humana cuando ya no pueda avanzar por otra vía. Para iniciar el goal, pega tú la línea.

```text
@olympus-goal-writer Convierte lo que acordamos en un goal para OpenCode.
/olympus.goal.write Convierte la investigación anterior en un goal para OpenCode.
```

El atajo es opcional y usa el mismo flujo de redacción.

## Publicar un pull request

[`olympus-git-pr-ready`](.opencode/skills/olympus-git-pr-ready/SKILL.md) abre o continúa un PR en GitHub, espera el CI e intenta corregir las fallas causadas por la tarea actual. Marca como bloqueos las fallas ajenas a la tarea y deja el PR abierto para que tú hagas el merge, salvo que lo solicites explícitamente. Requiere `git` y haber iniciado sesión en [GitHub CLI](https://cli.github.com/).

En OpenCode V2:

```text
@olympus-git-pr-ready Publica los cambios de la tarea actual y deja el PR listo para merge manual.
```

Con el atajo opcional instalado:

```text
/olympus.git.pr-ready Publica los cambios de la tarea actual y deja el PR listo para merge manual.
/olympus.git.pr-ready Publica los cambios de la tarea actual y mergea el PR a develop cuando cumpla las verificaciones y revisiones obligatorias.
```

## Trabajar con issues de GitHub

- [`olympus-git-issue-list`](.opencode/skills/olympus-git-issue-list/SKILL.md) ordena todos los issues abiertos, explica su prioridad y muestra los bloqueos y subissues sin modificar el backlog.
- [`olympus-git-issue-create`](.opencode/skills/olympus-git-issue-create/SKILL.md) convierte hallazgos en issues independientes o en uno o varios epics con subissues nativos. Pide un borrador para ver la estructura antes de publicar.
- [`olympus-git-issue-work`](.opencode/skills/olympus-git-issue-work/SKILL.md) trabaja en los issues que indiques o elige un grupo por prioridad y relación, implementa y prueba los cambios, y deja los PRs para merge manual salvo que lo pidas explícitamente.

Estas skills requieren haber iniciado sesión en GitHub CLI. Escribe `@` seguido del ID de la skill en tu solicitud, o instala los atajos opcionales y usa lenguaje natural:

```text
/olympus.git.issue-list
/olympus.git.issue-create Convierte la investigación anterior en issues y agrupa los hallazgos relacionados en epics.
/olympus.git.issue-work Trabaja en los issues #42 y #57.
/olympus.git.issue-work Comienza con 3 issues.
```

## Verificar el cumplimiento de una tarea

[`olympus-git-issue-check`](.opencode/skills/olympus-git-issue-check/SKILL.md) valida los cambios actuales contra el issue o la tarea acordada. Muestra qué pasó con evidencia, qué falta y qué excepciones se aceptaron explícitamente. Reporta por separado el porcentaje de cumplimiento original y el del alcance que sigue siendo obligatorio. Solo entrega el diagnóstico.

```text
@olympus-git-issue-check Valida los cambios actuales contra el issue #42.
/olympus.git.issue-check Verifica lo que acordamos y muestra las limitaciones aceptadas.
```

## Crear una skill

[`olympus-skill-author`](.opencode/skills/olympus-skill-author/SKILL.md) convierte un flujo de trabajo en una Agent Skill reutilizable o te ayuda a actualizar una skill existente. También puede crear un comando opcional para la skill que generes.

Abre este repositorio en OpenCode V2 y escribe una solicitud como esta:

```text
@olympus-skill-author Haz un borrador de una skill que genere notas de versión a partir de pull requests integrados. Muéstralo sin escribir archivos.
```

## Instalar en otro proyecto

1. Copia el `SKILL.md` elegido a `.opencode/skills/<id>/SKILL.md` en el proyecto destino y conserva el nombre de la carpeta de la skill. OpenCode la detectará en esa ruta.
2. Si quieres habilitar un atajo, copia solo el archivo del comando elegido a `.opencode/commands/` en el proyecto destino, con el mismo nombre. Usará la misma skill con el agente activo.

| Archivo de la skill | Archivo del atajo opcional |
| --- | --- |
| [`olympus-goal-writer/SKILL.md`](.opencode/skills/olympus-goal-writer/SKILL.md) | [`olympus.goal.write.md`](commands/olympus.goal.write.md) |
| [`olympus-git-issue-list/SKILL.md`](.opencode/skills/olympus-git-issue-list/SKILL.md) | [`olympus.git.issue-list.md`](commands/olympus.git.issue-list.md) |
| [`olympus-git-issue-create/SKILL.md`](.opencode/skills/olympus-git-issue-create/SKILL.md) | [`olympus.git.issue-create.md`](commands/olympus.git.issue-create.md) |
| [`olympus-git-issue-work/SKILL.md`](.opencode/skills/olympus-git-issue-work/SKILL.md) | [`olympus.git.issue-work.md`](commands/olympus.git.issue-work.md) |
| [`olympus-git-issue-check/SKILL.md`](.opencode/skills/olympus-git-issue-check/SKILL.md) | [`olympus.git.issue-check.md`](commands/olympus.git.issue-check.md) |
| [`olympus-git-pr-ready/SKILL.md`](.opencode/skills/olympus-git-pr-ready/SKILL.md) | [`olympus.git.pr-ready.md`](commands/olympus.git.pr-ready.md) |
| [`olympus-skill-author/SKILL.md`](.opencode/skills/olympus-skill-author/SKILL.md) | [`olympus.skill-author.md`](commands/olympus.skill-author.md) |

Copia solo los archivos que hayas elegido. Las guías `AGENTS.md` son para el mantenimiento de este repositorio. Para habilitar aquí el atajo, usa este repositorio como destino en el paso 2.

## Documentación

Lee esta guía [en inglés](README.md). Consulta [AGENTS.md](AGENTS.md) para conocer las convenciones del repositorio.

Referencias oficiales: [Skills de OpenCode](https://opencode.ai/docs/skills/), [Comandos de OpenCode](https://opencode.ai/docs/commands/) y la [especificación de Agent Skills](https://agentskills.io/specification).
