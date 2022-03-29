pgweb but container waits for the specified host to come up before starting pgweb

## Steps
- Build dockerfile
```bash
docker build -t pgweb .
```
- Run
```bash
docker run pgweb-new -e HOST=db_host DATABASE_URL=postgres://username:password@db_host:5432/db_name?sslmode=disable
```
