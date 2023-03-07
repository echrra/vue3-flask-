import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
const path = require("path")
// https://vitejs.dev/config/
export default defineConfig({
  root: 'src/pages/',
  envDir: process.cwd(),
  base: 
    process.env.VITE_NODE_ENV === "production"? "./": "",
  build: {
    chunkSizeWarningLimit:1500,
    assetsDir: "./assets",
    rollupOptions: {
      input: {
        p1: path.resolve(__dirname, "src/pages/index.html"),
        p2: path.resolve(__dirname, "src/pages/heartmovie.html"),
        p3: path.resolve(__dirname, "src/pages/user.html"),
      }
    },
  },
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server:{
    headers: {  //允许跨域访问
      'Access-Control-Allow-Origin': '*',
    },
    proxy: {
      '/api': {
        target: process.env.VITE_APP_URL ,
        // target就是你要访问的目标地址，可以是基础地址，这样方便在这个网站的其他api口调用数据
        ws: true,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
        // 要记得加rewrite这句
      },
    }
  },
  define:{
    'process.env':{}
  }
})
