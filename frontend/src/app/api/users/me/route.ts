import { backendRequest } from "@/lib/api-utilis";
import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const response = await backendRequest(request, {
    path: "/users/me",
    method: "GET",
    requiresAuth: true,
  });

  return response;
}
