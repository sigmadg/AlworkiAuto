<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const valid = ref(false);
const logform = ref();
const email = ref('');
// Reglas de validación de correo electrónico
const emailRules = ref([
  (v: string) => !!v.trim() || 'El correo electrónico es obligatorio',
  (v: string) => {
    const trimmedEmail = v.trim();
    return !/\s/.test(trimmedEmail) || 'El correo electrónico no debe contener espacios';
  },
  (v: string) => /.+@.+\..+/.test(v.trim()) || 'El correo electrónico debe ser válido'
]);

const router = useRouter();

function validate() {
  if (logform.value && logform.value.validate()) {
    router.push('/starter');
  }
}
</script>

<template>
  <h4 class="text-h4 my-4 mb-8 font-weight-regular text-medium-emphasis">
    Ingresa tu dirección de correo electrónico.
  </h4>
  <v-form ref="logform" lazy-validation v-model="valid" action="/starter" @submit.prevent="validate" class="mt-7 loginForm">
    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="Dirección de correo electrónico / Nombre de usuario"
      class="mt-4 mb-8"
      required
      hide-details="auto"
      variant="outlined"
      color="primary"
      @input="email = email.trim()"
    ></v-text-field>

    <v-btn color="secondary" block class="mt-2" variant="flat" size="large" :disabled="!valid" type="submit">
      Enviar correo
    </v-btn>
  </v-form>
  <div class="mt-5 text-end">
    <v-divider />
    <v-btn variant="plain" to="/login1" class="mt-2 text-capitalize mr-n2">¿Ya tienes una cuenta?</v-btn>
  </div>
</template>
