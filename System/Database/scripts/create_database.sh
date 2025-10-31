psql -h $1 -U admin -W -d postgres -f structure.sql
psql -h $1 -U admin -W -d dtps -f data.sql
psql -h $1 -U admin -W -d dtps -f triggers.sql
