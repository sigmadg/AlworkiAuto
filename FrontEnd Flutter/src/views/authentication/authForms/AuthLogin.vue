<script setup lang="ts">
import { ref } from 'vue';
import { Form } from 'vee-validate';
import type { SubmissionHandler } from 'vee-validate'; // Importación exclusiva de tipo
import Google from '@/assets/images/auth/social-google.svg';
import Facebook from "@/assets/images/auth/social-facebook.svg";
import Apple from "@/assets/images/auth/social-apple.svg";
import WhatsApp from "@/assets/images/auth/social-whatsapp.svg";
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth'; // Importar el store

// ... imports de imágenes y interface Card permanecen igual

const router = useRouter();
const authStore = useAuthStore(); // Instanciar el store

// Modificar la redirección en el login exitoso
router.push('/dashboard/default'); // Cambiar window.location.href por esto

// Declaración de las referencias reactivas
const email = ref('info@codedthemes.com'); // Cambia username a email
const password = ref('admin123');
const checkbox = ref(false);
const valid = ref(false);
const show1 = ref(false);

const loginWithGoogle = () => {
  // Lógica para autenticación con Apple
  console.log("Iniciando con Apple...");
  // Ejemplo:
  // useAuthStore().loginWithProvider('apple');
};

const loginWithWhatsApp = () => {
  // Lógica para autenticación con WhatsApp
  console.log("Iniciando con WhatsApp...");
  // Ejemplo:
  // useAuthStore().loginWithProvider('whatsapp');
};

const loginWithFacebook = () => {
  // Lógica para autenticación con Apple
  console.log("Iniciando con Apple...");
  // Ejemplo:
  // useAuthStore().loginWithProvider('apple');
};

const loginWithApple = () => {
  // Lógica para autenticación con WhatsApp
  console.log("Iniciando con WhatsApp...");
  // Ejemplo:
  // useAuthStore().loginWithProvider('whatsapp');
};

// Reglas de validación para la contraseña
const passwordRules = ref([
  (v: string) => !!v || 'La contraseña es obligatoria',
  (v: string) => v === v.trim() || 'La contraseña no puede comenzar ni terminar con espacios',
  (v: string) => v.length <= 10 || 'La contraseña debe tener menos de 10 caracteres'
]);

// Reglas de validación para el correo electrónico
const emailRules = ref([
  (v: string) => !!v.trim() || 'El correo electrónico es obligatorio',
  (v: string) => {
    const trimmedEmail = v.trim();
    return !/\s/.test(trimmedEmail) || 'El correo electrónico no debe contener espacios';
  },
  (v: string) => /.+@.+\..+/.test(v.trim()) || 'El correo electrónico debe ser válido'
]);

// Función de validación
const validate: SubmissionHandler = async (_, { setErrors }) => {
  email.value = email.value.trim();

  try {
    const response = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    });

    const responseData = await response.json();

    if (!response.ok) {
      const errorMessage = responseData.error || 'Credenciales inválidas';
      throw new Error(errorMessage);
    }

    // Manejo de datos de sesión
    const { session_id: sessionId, user } = responseData;

    // Actualizar store y localStorage
    authStore.setSession(sessionId, user);

    console.log('Inicio de sesión exitoso:', { sessionId, user });

    // Redirección única y consistente
    await router.push(authStore.returnUrl || '/dashboard/default');

  } catch (error) {
    console.error('Error en el login:', error);
    setErrors({
      apiError: error instanceof Error
          ? error.message
          : 'Error desconocido durante el login'
    });

    // Limpiar credenciales en caso de error
    password.value = '';
  }
};
</script>

<template>
  <v-container>
    <!-- Botones de redes sociales -->
    <v-row>
      <v-col cols="12" sm="6" md="3">
        <v-btn block color="primary" variant="outlined" class="text-lightText googleBtn" @click="loginWithGoogle">
          <img :src="Google" alt="google" style="width: 24px; height: 24px;" />
          <span class="ml-2">Google</span>
        </v-btn>
      </v-col>
      <v-col cols="12" sm="6" md="3">
        <v-btn block color="primary" variant="outlined" class="text-lightText googleBtn" @click="loginWithFacebook">
          <img :src="Facebook" alt="facebook" style="width: 24px; height: 24px;" />
          <span class="ml-2">Facebook</span>
        </v-btn>
      </v-col>
      <v-col cols="12" sm="6" md="3">
        <v-btn block color="primary" variant="outlined" class="text-lightText googleBtn" @click="loginWithApple">
          <img :src="Apple" alt="apple" style="width: 24px; height: 24px;" />
          <span class="ml-2">Apple</span>
        </v-btn>
      </v-col>
      <v-col cols="12" sm="6" md="3">
        <v-btn block color="primary" variant="outlined" class="text-lightText googleBtn" @click="loginWithWhatsApp">
          <img :src="WhatsApp" alt="whatsapp" style="width: 24px; height: 24px;" />
          <span class="ml-2">WhatsApp</span>
        </v-btn>
      </v-col>
    </v-row>

    <!-- Separador "O" -->
    <v-row>
      <v-col class="d-flex align-center">
        <v-divider class="custom-devider" />
        <v-btn variant="outlined" class="orbtn" rounded="md" size="small">O</v-btn>
        <v-divider class="custom-devider" />
      </v-col>
    </v-row>

    <!-- Formulario de inicio de sesión -->
    <h5 class="text-h5 text-center my-4 mb-8">Iniciar sesión con correo electrónico</h5>
    <Form @submit="validate" class="mt-7 loginForm" v-slot="{ errors, isSubmitting }">
      <v-text-field
          v-model="email"
          :rules="emailRules"
          label="Correo electrónico"
          class="mt-4 mb-8"
          required
          density="comfortable"
          hide-details="auto"
          variant="outlined"
          color="primary"
      ></v-text-field>
      <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Contraseña"
          required
          density="comfortable"
          variant="outlined"
          color="primary"
          hide-details="auto"
          :append-inner-icon="show1 ? '$eye' : '$eyeOff'"
          :type="show1 ? 'text' : 'password'"
          @click:append-inner="show1 = !show1"
          class="pwdInput"
      ></v-text-field>

      <div class="d-sm-flex align-center mt-2 mb-7 mb-sm-0">
        <v-checkbox
            v-model="checkbox"
            :rules="[(v: any) => !!v || 'Debes aceptar para continuar']"
            label="Recordarme"
            required
            color="primary"
            class="ms-n2"
            hide-details
        ></v-checkbox>
        <div class="ms-auto">
          <router-link to="/forgot-pwd1" class="text-primary text-decoration-none">¿Olvidaste tu contraseña?</router-link>
        </div>
      </div>
      <v-btn color="secondary" :loading="isSubmitting" block class="mt-2" variant="flat" size="large" :disabled="valid" type="submit">
        Iniciar sesión
      </v-btn>
      <div v-if="errors.apiError" class="mt-2">
        <v-alert color="error">{{ errors.apiError }}</v-alert>
      </div>
    </Form>

    <!-- Enlace para registrarse -->
    <div class="mt-5 text-end">
      <v-divider />
      <v-btn variant="plain" to="/register1" class="mt-2 text-capitalize mr-n2">¿No tienes una cuenta?</v-btn>
    </div>
  </v-container>
</template>

<style lang="scss">
.custom-devider {
  border-color: rgba(0, 0, 0, 0.08) !important;
}
.googleBtn {
  border-color: rgba(0, 0, 0, 0.08);
  margin: 30px 0 20px 0;
}
.outlinedInput .v-field {
  border: 1px solid rgba(0, 0, 0, 0.08);
  box-shadow: none;
}
.orbtn {
  padding: 2px 40px;
  border-color: rgba(0, 0, 0, 0.08);
  margin: 20px 15px;
}

.loginForm {
  .v-text-field .v-field--active input {
    font-weight: 500;
  }
}
</style>