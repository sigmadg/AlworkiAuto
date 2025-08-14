<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const valid = ref(false);
const logform = ref();
const password = ref('');
const conpassword = ref('');
const show1 = ref(false);

// Reglas de validación de contraseña
const passwordRules = ref([
  (v: string) => !!v || 'La contraseña es obligatoria',
  (v: string) => (v && v.length <= 10) || 'La contraseña debe tener menos de 10 caracteres'
]);

const confirmpasswordRules = ref([
  (v: string) => !!v || 'La confirmación de la contraseña es obligatoria',
  (v: string) => (v && v.length <= 10) || 'La contraseña debe tener menos de 10 caracteres'
]);

const router = useRouter();

function validate() {
  logform.value.validate();
  if (logform.value) {
    router.push('/starter');
  }
}
</script>

<template>
  <h4 class="text-h4 my-4 mb-8 font-weight-regular text-medium-emphasis">
    Ingresa tu dirección de correo electrónico a continuación y te enviaremos un código OTP para restablecer tu contraseña.
  </h4>
  <v-form ref="logform" lazy-validation v-model="valid" action="/starter" @submit.prevent="validate" class="mt-7 loginForm">
    <v-text-field
      v-model="password"
      :rules="passwordRules"
      label="Nueva contraseña"
      required
      variant="outlined"
      color="primary"
      hide-details="auto"
      :append-inner-icon="show1 ? '$eye' : '$eyeOff'"
      :type="show1 ? 'text' : 'password'"
      @click:append-inner="show1 = !show1"
      class="pwdInput mb-4"
    ></v-text-field>

    <v-text-field
      v-model="conpassword"
      :rules="confirmpasswordRules"
      label="Confirmar contraseña"
      required
      variant="outlined"
      color="primary"
      hide-details="auto"
      class="pwdInput"
    ></v-text-field>

    <v-btn color="secondary" block class="mt-5" variant="flat" size="large" :disabled="valid" type="submit">
      Restablecer contraseña
    </v-btn>
  </v-form>
</template>
