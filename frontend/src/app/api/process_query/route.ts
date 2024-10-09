// app/api/process_query/route.ts

import { NextResponse } from "next/server";
import axios from "axios";

export async function POST(req: Request) {
  try {
    const { query } = await req.json();

    // Replace with your backend URL
    const backendResponse = await axios.post(
      "http://localhost:8000/process_query",
      {
        query,
      }
    );

    const finalResponse = backendResponse.data.final_response;

    return NextResponse.json({ final_response: finalResponse });
  } catch (error) {
    console.error("Error in API route:", error);
    return NextResponse.json({
      final_response: "There was an error processing the request.",
    });
  }
}
