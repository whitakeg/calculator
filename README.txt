SCCM4910 coursework scaffold: getting started

1. Start in your own lab calculator repository. Keep its Git history and
   record the starting commit hash before making the coursework changes.
   Copy the supplied EVIDENCE.md template into your repository and complete it
   with your own results and explanations as you work.
2. Copy batch_runner.py and batch_calculator.py beside calculator.py.
3. Copy the pack's data/ folder into the repository.
4. Read the brief and the docstring in batch_calculator.py. Before implementing
   your chosen requirement, write a pytest test that fails for that missing
   behaviour. Choose your own inputs and expected results.
5. Week 6: configure GitHub Actions and capture that failing test locally and
   in CI, with the commit/run references, before fixing it. Staff will not
   open your private GitHub repository, so save PR pages and CI runs as
   PDFs/screenshots with short log excerpts in evidence/. Complete
   process_calculation yourself, using your four lab functions, then capture
   the passing runs. Keep the test in the final suite.
6. Try normal.csv and mixed.csv with the supplied runner.
7. Complete the other new pytest tests with independently chosen expected
   results, and explain your failure/fix in EVIDENCE.md.
8. Week 7: write a repeatable check script; call it locally, from a tracked
   pre-commit hook and from CI. Document hook installation in a fresh clone.
9. Week 8: install Docker yourself (Docker Desktop, or Docker Engine on
   Linux) and check it works. Create a Dockerfile and .dockerignore; build a tagged image and
   run both batches in containers, documenting input/output handling.
10. Week 9: add the image build and a batch smoke check to CI after the test
    gate. Check actual expected output and fail CI on a mismatch.
11. Use Week 10 support. Finish and commit documentation and development
    evidence, check a fresh checkout and the final CI run, then tag cw-v1.0.
    Afterwards, copy SUBMISSION.template.txt outside your repository, rename
    it SUBMISSION.txt and fill in the final hash/run/image/reproduction details.
    Submit three files to Moodle's DevOps Portfolio assignment by
    Friday 18 December 2026, 16:00 GMT: the source ZIP (including the hidden
    .git folder), SUBMISSION.txt, and a PDF/screenshot of the final CI run.

Until you complete the function, NotImplementedError is expected. It marks
your programming task. An import error for calculator means these files are
not beside the calculator.py from your lab repository, or the lab functions
are missing. Ask a demonstrator if you need help restoring the baseline.

batch_runner.py supplies the CSV file handling and loop. You do not need to
rewrite or assess its command-line/file-error handling. Complete the function
and demonstrate the batch behaviour through your own results and tests.
The function returns (status, result, error_code). On success, status is
"OK" and error_code is empty. The runner writes row,status,result,error_code.

Commands, after completing the function:
  python3 batch_runner.py data/normal.csv results.csv
  python3 batch_runner.py data/mixed.csv mixed-results.csv
  python3 -m pytest

In the Unix shell taught in the labs, capture operational evidence with:
  python3 batch_runner.py data/mixed.csv mixed-results.csv > summary.txt 2> errors.txt

Acknowledge the supplied files in the README. Develop your assessed code,
tests, automation, hook, Docker/CI configuration and reflection yourself.
Docker and the CI smoke test are required. No registry push or hosting is needed.
