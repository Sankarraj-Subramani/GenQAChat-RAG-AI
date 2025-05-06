/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    NEXT_PUBLIC_BACKEND_URL: process.env.CODESPACES
      ? `https://${process.env.CODESPACE_NAME}-8000.app.github.dev`
      : process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000',
  },
};

module.exports = nextConfig;
