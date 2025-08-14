<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const valid = ref(false);
const logform = ref();

const router = useRouter();

function validate() {
  logform.value.validate();
  if (logform.value) {
    router.push('/starter');
  }
}
</script>

<template>
  <h4 class="text-h4 my-4 font-weight-regular text-medium-emphasis">
    Hemos enviado instrucciones para recuperar la contraseña a tu correo electrónico.
  </h4>
  <v-form ref="logform" v-model="valid" lazy-validation action="/starter" class="mt-5 loginForm" @submit.prevent="validate">
    <v-btn color="secondary" block class="mt-2" variant="flat" size="large" :disabled="valid" type="submit">
      Abrir correo
    </v-btn>
  </v-form>
</template>