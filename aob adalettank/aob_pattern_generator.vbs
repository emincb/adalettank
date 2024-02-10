'Created by AikonCWD

Set oWSH = CreateObject("WScript.Shell")
Set oFSO = CreateObject("Scripting.FileSystemObject")

T = InputBox("Enter array of bytes nº 1:")
T = T & vbcrlf & InputBox("Enter array of bytes nº 2:")

X = 3
While MsgBox("Do you want to introduce another array of bytes?", vbYesNo, "AoB Pattern Generator") = vbYes
   T = T & vbcrlf & InputBox("Enter array of bytes nº " & X &":")
   X = X + 1
Wend

AoB = Split(T, vbcrlf)

F = ""
W = 0
X = 0
For i = 1 To Len(AoB(0))
   For u = 1 To UBound(AoB)
      If Mid(AoB(u), i, 1) <> Mid(AoB(0), i, 1) Then
         F = F & "?"
         W = W + 1
         X = 1
         Exit For
      End If
   Next
   If X <> 1 Then F = F & Mid(AoB(0), i, 1)
   X = 0
Next

Set File = oFSO.CreateTextFile("aob.txt")
   File.Write "Original array of bytes:" & vbcrlf & vbcrlf
   File.Write Replace(T, vbcrlf & vbcrlf, vbcrlf) & vbcrlf & vbcrlf
   File.Write "Total array of bytes: " & UBound(AoB) + 1 & vbcrlf
   File.Write "Total wildcards used: " & W & vbcrlf & vbcrlf
   File.Write "Your AoB Pattern:" & vbcrlf & vbcrlf & F
File.Close

'MsgBox F

If MsgBox("AoB Patter Generator finished" & vbcrlf & vbcrlf & "Do you want to open aob.txt file?", vbYesNo, "AoB Pattern Generator") = vbYes Then
   oWSH.Run "notepad.exe aob.txt"
End If