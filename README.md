# OTP Generator API

A simple Serverless Python API that generates a random 6-digit One-Time Password (OTP) and returns it in JSON format. It is designed to be lightweight and easily deployable using [Vercel](https://vercel.com/).

## Features

- Generates a random 6-digit OTP (e.g., `123456`).
- Returns the OTP in a JSON response.
- Configured with CORS (`Access-Control-Allow-Origin: *`) to be accessible from any frontend application.
- Ready for Serverless deployment on Vercel.

## API Endpoint / Usage

When you make a `GET` request to the endpoint, it will return a JSON response containing the generated OTP.

**Response format:**
```json
{
  "otp": 583921
}
```

## Running Locally

To run the API locally on your machine for testing:

1. Clone the repository and navigate to the project directory.
2. Run the Python script:
   ```bash
   python otp.py
   ```
3. The server will start running at `http://localhost:8000/api/otp` (or your root path).
4. You can visit `http://localhost:8000` in your browser or use `curl`/Postman to get an OTP.

## Deployment on Vercel

This repository includes a `vercel.json` configuration file, making it ready to be deployed instantly on Vercel as a Serverless Function.

1. Ensure you have the [Vercel CLI](https://vercel.com/cli) installed, or link this repository to your Vercel dashboard.
2. If using the CLI, simply run:
   ```bash
   vercel
   ```
3. Follow the prompts. The `vercel.json` file handles routing all requests to the `otp.py` function.

## License

This project is open-source and available under the [MIT License](LICENSE).
