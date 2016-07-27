# Time-Series Paper

Bafna Lab Convention:

1. In choosing citation keys, please do not use things like ronen2013learning, tc. as the convention is difficult, leads to duplication of bib entries and numerous problems when we are sharing our bib files (The same entry can show up with different keys). Use Ronen2013 (Last name of the first author capitalized, and full year). If there are multiple papers, use Ronen2013, Ronen2013b,...

2. Do not use \eqref{} which converts to (<eqnum>). Instead use Eq.~\ref{}.

3. Please put a ~between text and reference (e.g., alpha~\cite{}, or Eq.~\ref{}) for appropriate saving.

4. Put a period after paragraph.

5. As far as possible, use TexMed to obtain bib entries, so that all bib entries are similarly formatted.



Other Guidelines:

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

