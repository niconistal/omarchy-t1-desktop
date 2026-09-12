import QtQuick
import Quickshell
import Quickshell.Io

// Background service: keeps the T1Bridge Touch Bar renderer pointed at this
// plugin's desktop provider. The provider itself is t1-desktop-provider.
Item {
  id: root

  // Injected by omarchy-shell (the first-party service loader).
  property var shell: null

  readonly property string pluginDir: Qt.resolvedUrl(".").toString().replace(/^file:\/\//, "").replace(/\/$/, "")
  readonly property string setupScript: pluginDir + "/t1-desktop-setup"
  property string lastAction: ""
  property string lastOutput: ""

  function run(action) {
    if (setup.running) return "busy: " + root.lastAction
    root.lastAction = action
    root.lastOutput = ""
    setup.command = [root.setupScript, action]
    setup.running = true
    return "started " + action
  }

  Process {
    id: setup
    stdout: StdioCollector { onStreamFinished: root.lastOutput = text.trim() }
    stderr: StdioCollector { onStreamFinished: if (text.trim() !== "") console.warn("[nn.t1-desktop] " + text.trim()) }
    onExited: function(exitCode) {
      if (exitCode !== 0) console.warn("[nn.t1-desktop] " + root.lastAction + " exited with " + exitCode)
    }
  }

  Process {
    id: statusQuery
    command: [root.setupScript, "status"]
    stdout: StdioCollector { onStreamFinished: root.lastOutput = text.trim() }
  }

  Component.onCompleted: run("install")

  IpcHandler {
    target: "t1desktop"

    function install(): string { return root.run("install") }
    function uninstall(): string { return root.run("uninstall") }
    function last(): string { return root.lastAction + ": " + root.lastOutput }
    function status(): string {
      statusQuery.running = true
      return "querying; read with: omarchy-shell t1desktop last"
    }
  }
}
