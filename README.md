# 💻 Desarrollo de Interfaces
- Autor : Ainhoa Fernández Vadillo
- GitHub : [@ainhoafdez](https://github.com/ainhoafdez)
- [LinkedIn](https://www.linkedin.com/in/ainhoa-fernández-vadillo-1498ab2a5)
- [Texto preformateado y Código fuente](#texto-preformateado-y-código-fuente)
- [Enlace](#enlace)
- [Fichero Leeme.txt](leeme.txt)

---

## Markdown

# #h1
## ##h2
### ###h3

### Listas desordenadas con -
- item 1
  - item 1.2
- item 2

### Listas ordenadas con num.
1. item 1
2. item 2

### Lista ✅ con - [X]
- [ ] Hacer 1
- [X] Hacer 2
- [ ] Hacer 3

---

### Estilos de texto
**Negrita** o __Negrita__

*Cursiva* o _Cursiva_

**Negrita con *Cursiva***

~Tachado~

<sub>subindice</sub>

<sup>superindice</sup>

<ins>subrayado</ins>

> Esto es una cita o quote

Este tipo de callouts no funcionan en GitHub, pero sí en otras plataformas
>[ !info ] Nota informativa

> Esto es información relevante

### Texto preformateado y Código fuente

```
Esto es un texto preformateado
```

Inicializar un repositorio en git: `git init`


Código en Python:
```python
saludo = 'Hola mundo'
print(saludo)
```

### Enlace
Ejemplo de enlace interno

### Imagen
![Gatete](https://parrillagines.es/wp-content/uploads/2022/02/porque-un-gato-llora-mucho.jpg)

---

### Menciones
@github/pablopc93

Enlazo una nota al pie [^1]

Enlazo otra nota al pie [^nota]

[^1] Esta es la nota al pie
[^nota] Esta es la otra nota al pie

| En la Izq | En el Centro | En la Dcha |
| :--- | :---: | ---: |
| Dato 1 | Dato 2 | Dato 3 |
| Dato 4 | Dato 5 | Dato 6 |

<details>
<summary> Este es el resumen de la sección desplegable </summary>
  
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type     and scrambled it to make a type specimen book.
</details>

<details>
<summary> Código en Python </summary>
  
```python
saludo = 'Hola mundo'
print(saludo)
```
</details>

### Diagrama de flujo

```mermaid
graph TD;
A --> B;
A --> C;
B --> D;
C --> D;
```
