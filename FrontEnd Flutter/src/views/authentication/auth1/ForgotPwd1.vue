<script setup lang="ts">
import Logo from '@/layouts/full/logo/LogoMain.vue';
import AuthForgotPwd from '../authForms/AuthForgotPwd.vue';
</script>

<template>
  <v-row class="h-screen" no-gutters>
    <!---Parte Izquierda-->
    <v-col cols="12" lg="7" xl="7" class="d-flex align-center bg-lightprimary">
      <v-container>
        <div class="pa-0 pa-sm-12">
          <v-row justify="center">
            <v-col cols="12" lg="10" xl="6" md="7">
              <v-card elevation="0" class="loginBox">
                <v-card variant="outlined">
                  <v-card-text class="pa-9">
                    <!---Logo de la Parte Izquierda -->
                    <v-row>
                      <v-col cols="12" md="7" sm="7" order-sm="first" order="last" class="text-sm-start text-center">
                        <h2 class="text-secondary text-h2">Contraseña</h2>
                      </v-col>
                      <v-col class="text-sm-end text-center" sm="5" cols="12">
                        <Logo />
                      </v-col>
                    </v-row>
                    <!---Logo de la Parte Izquierda -->

                    <!---Formulario de la Parte Izquierda-->
                    <AuthForgotPwd />
                    <!---Formulario de la Parte Izquierda-->
                  </v-card-text>
                </v-card>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </v-container>
    </v-col>
    <!---Parte Izquierda-->
    <!---Parte Derecha-->
    <v-col cols="12" lg="5" xl="5" class="d-none d-lg-flex align-end justify-center bgpattern position-relative">
      <v-container class="pa-0 ma-0 fill-height">
        <div class="cardAnimation">
          <video autoplay loop muted playsinline class="videoBackground">
            <source src="@/assets/videos/intro.mp4" type="video/mp4">
            Tu navegador no soporta videos.
          </video>
        </div>
      </v-container>
    </v-col>
    <!---Parte Derecha-->
  </v-row>
</template>

<style lang="scss">
.loginBox {
  max-width: 475px;
  margin: 0 auto;
}

.cardAnimation {
  position: relative;
  width: 100%;
  height: 100vh; /* Asegura que el contenedor ocupe toda la altura de la pantalla */
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden; /* Evita que el video se salga del contenedor */

  .videoBackground {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%; /* Ajusta el ancho del video */
    max-width: 100%; /* Limita el ancho máximo */
    height: auto; /* Mantiene la proporción del video */
    object-fit: cover;
    transform: translate(-50%, -50%); /* Centra el video */
  }
}

.bgpattern {
  background: url('@/assets/images/auth/auth-pattern.svg') repeat;
}
</style>