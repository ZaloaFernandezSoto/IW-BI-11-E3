<script setup>
import { ref } from 'vue'
// Vuefire nos da 'useCollection' para sincronizar datos en tiempo real automágicamente
import { useCollection } from 'vuefire'
import { collection, addDoc, deleteDoc, doc } from 'firebase/firestore'
import { db } from './firebase'

// --- LÓGICA DE ESTADO Y FIREBASE ---

// 1. Conexión Reactiva a la colección 'agenda' de Firestore
// 'contactos' se actualizará solo si cambia algo en la base de datos (Realtime)
const contactos = useCollection(collection(db, 'agenda'))

// 2. Variables del formulario
const nuevoNombre = ref('')
const nuevoEmail = ref('')
const nuevoTelefono = ref('')

// 3. Función para AÑADIR contacto
async function agregarContacto() {
  // Validación simple HTML5
  if (nuevoNombre.value.trim() === '' || nuevoEmail.value.trim() === '') return;

  try {
    await addDoc(collection(db, 'agenda'), {
      nombre: nuevoNombre.value,
      email: nuevoEmail.value,
      telefono: nuevoTelefono.value || 'Sin teléfono',
      creado: Date.now() // Útil si luego quisieras ordenar
    })
    
    // Limpiar formulario
    nuevoNombre.value = ''
    nuevoEmail.value = ''
    nuevoTelefono.value = ''
  } catch (error) {
    console.error("Error al añadir contacto:", error);
    alert("Hubo un error al guardar el contacto.");
  }
}

// 4. Función para BORRAR contacto
async function borrarContacto(id) {
  if (confirm('¿Seguro que quieres eliminar este contacto?')) {
    try {
      await deleteDoc(doc(db, 'agenda', id))
    } catch (error) {
      console.error("Error al borrar:", error);
    }
  }
}
</script>

<template>
  <main class="contenedor-principal">
    <header class="encabezado">
      <h1>📒 Agenda Web E4b</h1>
      <p>Gestión de contactos</p>
    </header>

    <section class="seccion-formulario">
      <h2>Nuevo Contacto</h2>
      <form @submit.prevent="agregarContacto" class="formulario">
        <div class="campo">
          <label for="nombre">Nombre:</label>
          <input 
            id="nombre" 
            v-model="nuevoNombre" 
            type="text" 
            placeholder="Ej. Zaloa Fernández" 
            required 
            class="input-control"
          />
        </div>

        <div class="campo">
          <label for="email">Email:</label>
          <input 
            id="email" 
            v-model="nuevoEmail" 
            type="email" 
            placeholder="ejemplo@correo.com" 
            required 
            class="input-control"
          />
        </div>

        <div class="campo">
          <label for="telefono">Teléfono (Opcional):</label>
          <input 
            id="telefono" 
            v-model="nuevoTelefono" 
            type="tel" 
            placeholder="600 123 456" 
            class="input-control"
          />
        </div>

        <button type="submit" class="btn-guardar">💾 Guardar Contacto</button>
      </form>
    </section>

    <section class="seccion-lista">
      <h2>Mis Contactos ({{ contactos.length }})</h2>
      
      <div v-if="contactos.length === 0" class="mensaje-vacio">
        <p>No hay contactos en la agenda. ¡Añade uno arriba!</p>
      </div>

      <ul v-else class="lista-contactos">
        <li v-for="contacto in contactos" :key="contacto.id" class="tarjeta-contacto">
          <div class="datos-contacto">
            <h3>{{ contacto.nombre }}</h3>
            <p><strong>✉️ Email:</strong> <a :href="'mailto:' + contacto.email">{{ contacto.email }}</a></p>
            <p><strong>📞 Tel:</strong> {{ contacto.telefono }}</p>
          </div>
          <button @click="borrarContacto(contacto.id)" class="btn-borrar">🗑️ Eliminar</button>
        </li>
      </ul>
    </section>
  </main>
</template>

<style>
/* CSS Limpio y semántico */

</style>