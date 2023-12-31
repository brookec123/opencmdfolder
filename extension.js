const vscode = require('vscode');
const path = require('path');
const cp = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('opencmdfolder.openCmdFolder', () => {
        const activeTextEditor = vscode.window.activeTextEditor;

        if (activeTextEditor) {
            const folderPath = path.dirname(activeTextEditor.document.uri.fsPath);

            // Path to your Python script
            const pythonScriptPath = path.join(__dirname, 'extension.py');

            // Run the Python script
            const pythonProcess = cp.spawn('python', [pythonScriptPath, folderPath]);

        } else {
            vscode.window.showInformationMessage('No active editor found.');
        }
    });

    context.subscriptions.push(disposable);
}

function deactivate() {
    // Cleanup logic, if any
}

module.exports = {
    activate,
    deactivate
};
