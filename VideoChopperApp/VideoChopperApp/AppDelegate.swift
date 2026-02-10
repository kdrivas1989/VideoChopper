import Cocoa
import WebKit

@main
class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!
    var webView: WKWebView!
    var serverProcess: Process?

    func applicationDidFinishLaunching(_ notification: Notification) {
        // Start Python server
        startServer()

        // Wait for server to start
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            self.createWindow()
        }
    }

    func startServer() {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/python3")

        // Get the app bundle's Resources path
        let resourcePath = Bundle.main.resourcePath ?? ""
        let mainPyPath = (resourcePath as NSString).appendingPathComponent("main.py")

        process.arguments = [mainPyPath]
        process.currentDirectoryURL = URL(fileURLWithPath: resourcePath)

        // Set environment
        var env = ProcessInfo.processInfo.environment
        env["FLASK_ENV"] = "production"
        process.environment = env

        do {
            try process.run()
            serverProcess = process
        } catch {
            print("Failed to start server: \(error)")
        }
    }

    func createWindow() {
        // Create window
        let windowRect = NSRect(x: 0, y: 0, width: 1400, height: 900)
        window = NSWindow(
            contentRect: windowRect,
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )
        window.title = "Video Chopper"
        window.center()

        // Create WebView
        let config = WKWebViewConfiguration()
        config.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")

        webView = WKWebView(frame: window.contentView!.bounds, configuration: config)
        webView.autoresizingMask = [.width, .height]

        window.contentView?.addSubview(webView)

        // Load the local server
        if let url = URL(string: "http://127.0.0.1:8080") {
            webView.load(URLRequest(url: url))
        }

        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    func applicationWillTerminate(_ notification: Notification) {
        serverProcess?.terminate()
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true
    }
}
