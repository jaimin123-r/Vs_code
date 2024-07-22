import java.io.*;
import java.net.*;
import java.util.*;

public class Example {
    private static final int PORT = 5500;
    private static final Set<PrintWriter> writers = new HashSet<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server started on port " + PORT);
            while (true) {
                new ClientHandler(serverSocket.accept()).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class ClientHandler extends Thread {
        private final Socket clientSocket;
        private PrintWriter out;

        public ClientHandler(Socket socket) {
            this.clientSocket = socket;
        }

        @Override
        public void run() {
            try {
                out = new PrintWriter(clientSocket.getOutputStream(), true);
                writers.add(out);
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

                String message;
                while ((message = in.readLine()) != null) {
                    for (PrintWriter writer : writers) {
                        writer.println(message);
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (out != null) {
                    writers.remove(out);
                }
                try {
                    clientSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
