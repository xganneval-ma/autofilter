import typescript from "@rollup/plugin-typescript";
import * as path from "path";
import { typescriptPaths } from "rollup-plugin-typescript-paths";
import { visualizer } from "rollup-plugin-visualizer";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    // Required to ensure baseUrl typescript option is properly handled by vite
    tsconfigPaths(),
  ],
  // https://vitejs.dev/guide/build.html#library-mode
  build: {
    lib: {
      entry: path.resolve(__dirname, "src/main.ts"),
      fileName: "main",
      formats: ["es", "cjs"],
    },
    rollupOptions: {
      external: [],
      plugins: [
        typescriptPaths({
          preserveExtensions: true,
        }),
        typescript({
          sourceMap: false,
          declaration: true,
          outDir: "dist",
          exclude: ["**/__tests__"],
        }),
        visualizer(),
      ],
    },
  },
});
