on run
    set appPath to (path to me as string) & "Contents:Resources:"
    set posixPath to POSIX path of appPath
    
    -- Start the Python server
    do shell script "cd " & quoted form of posixPath & " && /usr/bin/python3 app.py &> /dev/null &"
    
    -- Wait for server to start
    delay 2
    
    -- Open in browser
    open location "http://127.0.0.1:5050"
end run
