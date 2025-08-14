<script setup lang="ts">
import Appbar from './Components/AppBarMenu.vue';
import BannerInnerpage from './Components/BannerInnerpage.vue';
</script>

<template>
  <v-layout>
    <Appbar />
    <BannerInnerpage title="Política de Privacidad" subtitle="Última actualización: 11 de Marzo de 2025">
      <div>
        <v-card elevation="5" class="pa-6 text-body-1">
          <p>
            Esta Política de Privacidad rige la manera en que Alworki recopila, utiliza, mantiene y divulga la información obtenida de los usuarios de nuestra aplicación de profesiones y servicios.
          </p>

          <h3 class="text-h3 my-4">1. Información que Recopilamos</h3>
          <p>
            Recopilamos información que nos proporcionas directamente, así como información que se genera automáticamente cuando utilizas
            la Aplicación. Esta información puede incluir:
          </p>
          <ul class="ms-5 my-5">
            <li>
              <strong>Información personal:</strong> Nombre, dirección de correo electrónico, número de teléfono, dirección física, método
              de pago (tarjeta de crédito/débito), y cualquier otra información que nos proporciones al registrarte o utilizar la Aplicación.
            </li>
            <li>
              <strong>Información de transacciones:</strong> Detalles de los pedidos, historial de compras, y registros de servicios contratados.
            </li>
            <li>
              <strong>Información de ubicación:</strong> Si lo permites, recopilamos tu ubicación en tiempo real para garantizar tu seguridad y la de nuestros colaboradores.
            </li>
            <li>
              <strong>Información técnica:</strong> Dirección IP, tipo de dispositivo, sistema operativo, navegador, y datos de uso de la
              Aplicación.
            </li>
          </ul>

          <h3 class="text-h3 my-4">2. Uso de la Información</h3>
          <p>
            Utilizamos la información recopilada para los siguientes fines:
          </p>
          <ul class="ms-5 my-5">
            <li>Procesar y gestionar pedidos de productos y servicios.</li>
            <li>Facilitar operaciones entre usuarios.</li>
            <li>Mejorar la experiencia del usuario y personalizar la Aplicación.</li>
            <li>Enviar notificaciones, actualizaciones y promociones relacionadas con la Aplicación.</li>
            <li>Cumplir con obligaciones legales y resolver disputas.</li>
          </ul>

          <h3 class="text-h3 my-4">3. Intercambio de Favores</h3>
          <p>
            La Aplicación permite a los usuarios intercambiar favores, como la prestación de servicios, sin
            necesidad de transacciones monetarias. Al utilizar esta funcionalidad, aceptas que:
          </p>
          <ul class="ms-5 my-5">
            <li>La información relacionada con el intercambio de favores (como descripciones, ubicaciones y horarios) será visible para los
              usuarios involucrados.</li>
            <li>Nos reservamos el derecho de moderar y supervisar los intercambios para garantizar la seguridad y el cumplimiento de
              nuestras políticas.</li>
          </ul>

          <h3 class="text-h3 my-4">4. Cookies y Tecnologías Similares</h3>
          <p>
            Utilizamos cookies y tecnologías similares para mejorar la funcionalidad de la Aplicación, analizar el tráfico y personalizar
            la experiencia del usuario. Puedes gestionar o desactivar las cookies a través de la configuración de tu navegador, pero esto
            podría afectar el funcionamiento de la Aplicación.
          </p>

          <h3 class="text-h3 my-4">5. Compartir Información</h3>
          <p>
            No vendemos ni alquilamos tu información personal a terceros. Sin embargo, podemos compartir información en las siguientes
            circunstancias:
          </p>
          <ul class="ms-5 my-5">
            <li>Con proveedores de servicios que nos ayudan a operar la Aplicación (por ejemplo, procesadores de pagos.</li>
            <li>Con autoridades competentes cuando sea requerido por ley o para proteger nuestros derechos y seguridad.</li>
            <li>En caso de una fusión, adquisición o venta de activos, tu información podría ser transferida al nuevo propietario.</li>
          </ul>

          <h3 class="text-h3 my-4">6. Seguridad de la Información</h3>
          <p>
            Implementamos medidas de seguridad técnicas y organizativas para proteger tu información contra accesos no autorizados,
            alteraciones o destrucción. Sin embargo, ninguna medida de seguridad es infalible, por lo que no podemos garantizar la
            seguridad absoluta de tus datos.
          </p>

          <h3 class="text-h3 my-4">7. Tus Derechos</h3>
          <p>
            Tienes derecho a acceder, corregir, eliminar o limitar el uso de tu información personal. También puedes oponerte al
            procesamiento de tus datos o solicitar la portabilidad de los mismos. Para ejercer estos derechos, contáctanos a través de
            [correo electrónico de contacto].
          </p>

          <h3 class="text-h3 my-4">8. Cambios en esta Política</h3>
          <p>
            Nos reservamos el derecho de actualizar esta Política de Privacidad en cualquier momento. Te notificaremos de cambios
            significativos a través de la Aplicación o por correo electrónico. El uso continuado de la Aplicación después de dichos cambios
            constituye tu aceptación de la Política actualizada.
          </p>

          <h3 class="text-h3 my-4">9. Contacto</h3>
          <p>
            Si tienes preguntas sobre esta Política de Privacidad o el manejo de tus datos, contáctanos en:
            <a href="mailto:privacidad@tuaplicacion.com">privacidad@tuaplicacion.com</a>.
          </p>

          <h3 class="text-h3 my-4">11 de Marzo de 2025</h3>
        </v-card>
      </div>
    </BannerInnerpage>
  </v-layout>
</template>