# Time-Series Paper
Guidelines:

1. To avoid conflicts create your branch
```
git checkout -b [name_of_your_new_branch, e.g., arya]
```
and after your commits puch by
```
git push origin [name_of_your_new_branch]
```

2. Limit lined to 80 chrs. If you are using `TexStudio`, go to `Configure TexStudio>Adv Editor>Line Wrapping` then select `Hard`.

3. If you are using `TexStudio`,  create a macro for push and set the trigger to `?close-file`
```
dialog = new UniversalInputDialog()
dialog.setWindowTitle("Git commit")
dialog.add("", "Comment", "comment")
if (dialog.exec() != null) {
    comment = dialog.get("comment")
    buildManager.runCommand("git commit -a -m \"" + comment + "\"", editor.fileName())
    buildManager.runCommand("git push origin [name_of_your_new_branch]", editor.fileName())
    }
```
which you can also run it from menu bar.

