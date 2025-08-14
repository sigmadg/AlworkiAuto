<script setup lang="ts">
import { ref } from 'vue';
import Google from '@/assets/images/auth/social-google.svg';
import Facebook from "@/assets/images/auth/social-facebook.svg";
import Apple from "@/assets/images/auth/social-apple.svg";
import WhatsApp from "@/assets/images/auth/social-whatsapp.svg";

const checkbox = ref(false);
const show1 = ref(false);
const password = ref('');
const email = ref('');
const Regform = ref();
const firstname = ref('');
const lastname = ref('');
const errorMessage = ref(''); // Variable para almacenar el mensaje de error
const showError = ref(false); // Variable para controlar la visibilidad del mensaje de error
const showSuccessModal = ref(false); // Controlar la visibilidad del modal de éxito


// Reglas de validación de contraseña
const passwordRules = ref([
  (v: string) => !!v || 'La contraseña es obligatoria',
  (v: string) => v === v.trim() || 'La contraseña no puede comenzar ni terminar con espacios',
  (v: string) => v.length <= 10 || 'La contraseña debe tener menos de 10 caracteres'
]);

// Reglas de validación de correo electrónico
const emailRules = ref([
  (v: string) => !!v.trim() || 'El correo electrónico es obligatorio',
  (v: string) => {
    const trimmedEmail = v.trim();
    return !/\s/.test(trimmedEmail) || 'El correo electrónico no debe contener espacios';
  },
  (v: string) => /.+@.+\..+/.test(v.trim()) || 'El correo electrónico debe ser válido'
]);

// Función para enviar el formulario de registro
async function register() {
  // Validar el formulario
  const { valid } = await Regform.value.validate();
  if (!valid) {
    errorMessage.value = 'El formulario no es válido. Por favor, revisa los campos.'; // Mensaje de error
    showError.value = true; // Mostrar el mensaje de error
    return;
  }

  try {
    const response = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        firstname: firstname.value,
        lastname: lastname.value,
        email: email.value,
        password: password.value,
      }),
    });

    if (!response.ok) {
      throw new Error('Error en el registro');
    }

    const data = await response.json();
    console.log('Registro exitoso:', data);
    alert('Registro exitoso'); // Mostrar un mensaje al usuario
  } catch (error) {
    errorMessage.value = 'Error en el registro. Por favor, inténtalo de nuevo.'; // Mensaje de error
    showError.value = true; // Mostrar el mensaje de error
    console.error('Error:', error);
  }
}

// Funciones para manejar el inicio de sesión con redes sociales
function loginWithGoogle() {
  console.log('Iniciar sesión con Google');
  // Aquí puedes integrar la lógica para autenticación con Google
}

function loginWithFacebook() {
  console.log('Iniciar sesión con Facebook');
  // Aquí puedes integrar la lógica para autenticación con Facebook
}

function loginWithApple() {
  console.log('Iniciar sesión con Apple');
  // Aquí puedes integrar la lógica para autenticación con Apple
}

function loginWithWhatsApp() {
  console.log('Iniciar sesión con WhatsApp');
  // Aquí puedes integrar la lógica para autenticación con WhatsApp
}
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

    <!-- Formulario de registro -->
    <h5 class="text-h5 text-center my-4 mb-8">Registrarse con correo electrónico</h5>
    <v-form ref="Regform" lazy-validation class="mt-7 loginForm">
      <v-row>
        <v-col cols="12" sm="6">
          <v-text-field
              v-model="firstname"
              density="comfortable"
              hide-details="auto"
              variant="outlined"
              color="primary"
              label="Nombre"
              required
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field
              v-model="lastname"
              density="comfortable"
              hide-details="auto"
              variant="outlined"
              color="primary"
              label="Apellido"
              required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-text-field
          v-model="email"
          :rules="emailRules"
          label="Dirección de correo electrónico"
          class="mt-4 mb-4"
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

      <div class="d-sm-inline-flex align-center mt-2 mb-7 mb-sm-0 font-weight-bold">
        <v-checkbox
            v-model="checkbox"
            :rules="[(v: any) => !!v || '¡Debes aceptar para continuar!']"
            label="¿Aceptas los?"
            required
            color="primary"
            class="ms-n2"
            hide-details
        ></v-checkbox>
        <router-link to="/privacy-policy" class="ms-1 text-lightText">Términos y Condiciones</router-link>
      </div>

      <v-btn color="secondary" block class="mt-2" variant="flat" size="large" @click="register">Registrarse</v-btn>
    </v-form>

    <!-- Modal de éxito -->
    <v-dialog v-model="showSuccessModal" max-width="500">
      <v-card>
        <v-card-title class="headline">¡Registro exitoso!</v-card-title>
        <v-card-text>
          Te has registrado correctamente. Revisa tu correo electrónico para el mensaje de bienvenida.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="showSuccessModal = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Enlace para iniciar sesión -->
    <div class="mt-5 text-end">
      <v-divider />
      <v-btn variant="plain" to="/login1" class="mt-2 text-capitalize mr-n2">¿Ya tienes una cuenta?</v-btn>
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