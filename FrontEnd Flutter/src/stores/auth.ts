// stores/auth.ts (Versión corregida)
import { defineStore } from 'pinia';
import { router } from '@/router';

interface User {
  id: number;
  firstname: string;
  lastname: string;
  email: string;
}

interface LoginResponse {
  session_id: string;
  user: User;
  message?: string;  // Para mensajes genéricos
  error?: string;    // Específico para errores
}

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: JSON.parse(localStorage.getItem('user') || 'null') as User | null,
    sessionId: localStorage.getItem('session_id'), // Tipo inferido: string | null
    returnUrl: null as string | null
  }),

  actions: {
    // Verificación mejorada de tipos
    setSession(sessionId: string, userData: User) {
      this.sessionId = sessionId;
      this.user = userData;
      localStorage.setItem('session_id', sessionId);
      localStorage.setItem('user', JSON.stringify(userData));

      const redirectUrl = this.returnUrl || '/dashboard/default';
      router.push(redirectUrl);
    },

    async verifySession() {
      if (!this.sessionId) { // Verificación de null
        this.logout();
        return;
      }

      try {
        const response = await fetch('http://localhost:5000/verify-session', {
          headers: {
            'Authorization': `Bearer ${this.sessionId}` // sessionId es string aquí
          }
        });

        if (!response.ok) throw new Error('Sesión inválida');

        // Actualizar datos del usuario
        const data = await response.json() as User;
        this.user = data;

        // eslint-disable-next-line @typescript-eslint/no-unused-vars
      } catch (error) {
        this.logout();
      }
    },

    async login(email: string, password: string) {
      try {
        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });

        const data: LoginResponse = await response.json();

        if (!response.ok) {
          // 3. Usar ambos campos posibles para mensajes de error
          const errorMessage = data.error || data.message || 'Error de autenticación';
          throw new Error(errorMessage);
        }

        if (!data.session_id || !data.user) {
          throw new Error('Respuesta del servidor inválida');
        }

        this.setSession(data.session_id, data.user);

      } catch (error) {
        console.error('Error en login:', error);
        throw error;
      }
    },

    logout() {
      this.user = null;
      this.sessionId = null;
      localStorage.removeItem('session_id');
      localStorage.removeItem('user');
      router.push('/login');
    }
  }
});