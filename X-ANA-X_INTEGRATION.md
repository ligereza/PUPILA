# Integración con X-ANA-X

## Fuente canónica

La integración canónica vive en:

https://github.com/ligereza/X-ANA-X/tree/PUPILA

La rama PUPILA de X-ANA-X contiene el núcleo común y dos superficies:

- PUPILA/assistance: asociación de tareas entre una interfaz conocida y otra
  por aprender; devuelve candidatos, evidencia y ambigüedad sin ejecutar.
- PUPILA/visual: geometría, medición y representación perceptual que alimenta
  la asistencia.

Este repositorio separado conserva principalmente la implementación de
asistencia. El trabajo visual integrado se mantiene en PUPILA/visual dentro
de X-ANA-X; no se debe crear aquí otra copia con otro nombre.

## Mapa de ramas

| Rama de este repositorio | Destino en X-ANA-X |
|---|---|
| main | PUPILA/PUPILA/assistance |
| fix/ambiguity-consistency | PUPILA/PUPILA/assistance |

El núcleo compartido se recibe desde X-ANA-X/core. Una mejora que afecte
varias superficies debe comenzar en X-ANA-X, no duplicarse aquí.

## Cómo portar trabajo

1. Trabajar en la rama de dominio correspondiente.
2. Ejecutar la prueba local y registrar el commit.
3. Portar ese commit a X-ANA-X/PUPILA, conservando la procedencia.
4. Si el cambio modifica el contrato común, portarlo primero a X-ANA-X/main
   y luego a las ramas consumidoras.

No copiar datos privados, caches ni worktrees. No ejecutar acciones sobre la
aplicación anfitriona: PUPILA produce una propuesta revisable.

## Validación

Desde la raíz de este repositorio:

PYTHONPATH=src python -m unittest discover -s tests -v
