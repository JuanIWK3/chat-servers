import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class ServerThread extends Thread {
    private Socket socket;
    private String name;

    public ServerThread(Socket socket) {
        this.socket = socket;
    }

    public void run() {

        try (InputStream input = socket.getInputStream()) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            OutputStream writer = socket.getOutputStream();

            String askName = "Enter your name: ";

            while (this.name == null) {
                writer.write(askName.getBytes());
                this.name = reader.readLine();
                writer.write('\n');
            }

            while (true) {
                String line = reader.readLine();
                if (line == null || line.length() == 0) {
                    break;
                }

                line = this.name + ": " + line + "\n";

                System.out.print(line);
            }

        } catch (IOException e) {
            System.out.print("Exception" + e);
            e.printStackTrace();
        }
    }
}
