# 📸 Sistema de Imágenes para Recetas

## ✅ Cambios Realizados

### 1. Modelo de Base de Datos
Se añadió el campo `imagen` al modelo `Receta`:
- **Tipo**: CharField (máximo 500 caracteres)
- **Permite valores nulos**: Sí (opcional)
- **Descripción**: Almacena solo el nombre del archivo de imagen

### 2. Migración Aplicada
- ✅ Migración `0003_receta_imagen.py` creada y aplicada
- ✅ Columna `imagen` añadida a la tabla de recetas

### 3. Panel de Administración Mejorado
Se actualizó `admin.py` con:
- Campo `imagen` visible en el listado de recetas
- Instrucciones claras sobre cómo añadir imágenes
- Organización en fieldsets para mejor usabilidad

### 4. Plantillas Actualizadas
Todas las plantillas ahora muestran imágenes dinámicamente:
- ✅ `index.html` - Página de inicio
- ✅ `lista_recetas.html` - Lista de recetas
- ✅ `detalle_receta.html` - Detalle de receta
- ✅ `detalle_tipo_plato.html` - Recetas por categoría
- ✅ `detalle_ingrediente.html` - Recetas con un ingrediente

## 📁 Cómo Usar el Sistema de Imágenes

### Paso 1: Preparar la Imagen
1. Redimensiona tu imagen (recomendado: 800x600px)
2. Guárdala con un nombre descriptivo (ej: `paella.jpg`, `tortilla-patatas.jpg`)
3. Formatos aceptados: `.jpg`, `.jpeg`, `.png`, `.webp`

### Paso 2: Guardar en la Carpeta Correcta
Coloca la imagen en:
```
appRecipesStore/static/appRecipesStore/img/
```

Por ejemplo:
```
appRecipesStore/static/appRecipesStore/img/paella.jpg
appRecipesStore/static/appRecipesStore/img/tortilla.jpg
```

### Paso 3: Registrar en el Admin de Django
1. Accede al admin: `http://localhost:8000/admin/`
2. Ve a **Recetas** → Selecciona la receta
3. En el campo **Imagen**, escribe **solo el nombre del archivo**: `paella.jpg`
4. Guarda los cambios

## ⚠️ Importante

### ✅ Correcto:
```
paella.jpg
tortilla-patatas.png
croquetas.webp
```

### ❌ Incorrecto:
```
/static/appRecipesStore/img/paella.jpg        ← No incluir la ruta completa
static/appRecipesStore/img/paella.jpg         ← No incluir static/
img/paella.jpg                                ← No incluir img/
```

## 🖼️ Imagen por Defecto
Si una receta no tiene imagen asignada, se mostrará automáticamente:
```
appRecipesStore/img/recepie/recepie_1.png
```

## 📋 Ejemplo Completo

### 1. Guardas la imagen:
```
📁 appRecipesStore/static/appRecipesStore/img/
   └── paella-valenciana.jpg
```

### 2. En el admin de Django:
```
Campo "Imagen": paella-valenciana.jpg
```

### 3. En el HTML se genera:
```html
<img src="/static/appRecipesStore/img/paella-valenciana.jpg" alt="Paella Valenciana">
```

## 🎯 Recomendaciones

1. **Nombres de archivo**: Usa minúsculas y guiones (sin espacios)
   - ✅ `paella-valenciana.jpg`
   - ❌ `Paella Valenciana.jpg`

2. **Tamaño de archivo**: Mantén las imágenes bajo 500KB para carga rápida

3. **Formato**: Usa `.webp` para mejor compresión, o `.jpg` como alternativa

4. **Dimensiones**: 800x600px es ideal para el diseño actual

## 🔧 Estructura de Carpetas

```
RecipesStore/
├── appRecipesStore/
│   └── static/
│       └── appRecipesStore/
│           └── img/              ← AQUÍ van tus imágenes de recetas
│               ├── paella.jpg
│               ├── tortilla.jpg
│               └── recepie/
│                   └── recepie_1.png  ← Imagen por defecto
```

---

**¡Listo!** Ahora tu sitio web mostrará las imágenes de cada receta de forma dinámica. 🎉
