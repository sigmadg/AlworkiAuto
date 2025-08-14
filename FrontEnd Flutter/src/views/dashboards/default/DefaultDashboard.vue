<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

// Importación correcta de assets en Vite
import image1 from '@/assets/images/cards/1.svg?url'; // Agrega ?url
import image2 from '@/assets/images/cards/2.svg?url';
import image3 from '@/assets/images/cards/3.svg?url';

interface Card {
  title: string;
  description: string;
  last_updated: string;
  image_name: string;
  address: string;
}

const router = useRouter();
const cards = ref<Card[]>([]);

// Mapeo corregido
const imageMap: Record<string, string> = {
  '1.svg': image1,
  '2.svg': image2,
  '3.svg': image3,
};

console.log('Mapeo de imágenes:', imageMap);

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/cards');
    // Verifica la estructura de los datos recibidos
    console.log('Datos de la API:', response.data);
    cards.value = response.data;
  } catch (error) {
    console.error('Error fetching cards:', error);
  }
});

const getImageUrl = (imageName: string) => {
  const url = imageMap[imageName];
  console.log('Buscando imagen:', imageName, 'Encontrada:', url); // Debug
  return url || '';
};

const redirectTo = (address: string) => {
  router.push(address);
};
</script>

<template>
  <v-row>
    <v-col v-for="(card, index) in cards" :key="index" cols="12" lg="4">
      <v-card variant="outlined" class="overflow-hidden">
        <!-- Imagen primero con altura fija -->
        <v-img
            :src="getImageUrl(card.image_name)"
            cover
            height="200"
            class="mb-4"
        />

        <v-card-item>
          <v-card-title class="text-h4">{{ card.title }}</v-card-title>
        </v-card-item>

        <v-card-text>
          <p class="text-medium-emphasis mb-4">{{ card.description }}</p>
          <div class="text-caption text-medium-emphasis">
            {{ card.last_updated }}
          </div>

          <v-btn
              color="primary"
              class="mt-4"
              @click="redirectTo(card.address)"
              block
          >
            Continuar
          </v-btn>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>