

CREATE OR REPLACE TABLE Customers
(
  customer_id SMALLINT    NOT NULL,
  first_name  VARCHAR(45) NOT NULL,
  last_name   VARCHAR(45) NOT NULL,
  birth_date  DATE        NOT NULL,
  email       VARCHAR(50) NOT NULL,
  phone       VARCHAR(12) NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE OR REPLACE TABLE Games
(
  game_id      SMALLINT      NOT NULL,
  release_year DATE          NOT NULL,
  min_players  TINYINT       NOT NULL,
  max_players  TINYINT       NOT NULL,
  play_time    VARCHAR(50)   NOT NULL,
  min_age      TINYINT       NOT NULL,
  price        DECIMAL       NOT NULL,
  title        VARCHAR(100)  NOT NULL,
  description  VARCHAR(10000) NOT NULL,
  type         VARCHAR(18)   NOT NULL,
  PRIMARY KEY (game_id)
);

CREATE OR REPLACE TABLE Tournament_schedule
(
  tournament_id SMALLINT NOT NULL,
  date          DATE     NOT NULL,
  PRIMARY KEY (tournament_id)
);

CREATE OR REPLACE TABLE Tournaments
(
  tournament_id SMALLINT NOT NULL,
  game_id       SMALLINT NOT NULL,
  max_players   TINYINT  NOT NULL,
  entry_fee     DECIMAL  NOT NULL,
  prize        DECIMAL  NOT NULL,
  PRIMARY KEY (tournament_id)
);


CREATE OR REPLACE TABLE Tournaments_results
(
  tournament_id SMALLINT NOT NULL,
  place         SMALLINT NOT NULL,
  customer_id   SMALLINT NOT NULL,
  PRIMARY KEY (tournament_id, place)
);

CREATE OR REPLACE TABLE Rentals
(
  rental_id    SMALLINT NOT NULL,
  payment_id   INT      NOT NULL,
  employee_id  SMALLINT NOT NULL,
  customer_id  SMALLINT NOT NULL,
  inventory_id SMALLINT NOT NULL,
  rental_date  DATE     NOT NULL,
  return_date  DATE     NULL    ,
  PRIMARY KEY (rental_id)
);

CREATE OR REPLACE TABLE Sales
(
  payment_id   INT      NOT NULL,
  employee_id  SMALLINT NOT NULL,
  customer_id  SMALLINT NOT NULL,
  inventory_id SMALLINT NOT NULL,
  PRIMARY KEY (payment_id)
);

CREATE OR REPLACE TABLE Inventory
(
  inventory_id SMALLINT    NOT NULL,
  game_id      SMALLINT    NOT NULL,
  type         VARCHAR(50) NULL    ,
  PRIMARY KEY (inventory_id)
);

CREATE OR REPLACE TABLE Finances
(
  payment_id INT          NOT NULL,
  in_out     TINYINT(1)   NOT NULL,
  value      DECIMAL      NOT NULL,
  date       DATE         NOT NULL,
  title      VARCHAR(100) NOT NULL,
  PRIMARY KEY (payment_id)
);

CREATE OR REPLACE TABLE Employees
(
  employee_id     SMALLINT    NOT NULL,
  first_name      VARCHAR(45) NOT NULL,
  last_name       VARCHAR(50) NOT NULL,
  start_work_date DATE        NOT NULL,
  end_work_date   DATE        NULL    ,
  email           VARCHAR(45) NOT NULL,
  phone           INT         NOT NULL,
  address_id      SMALLINT    NOT NULL,
  birth_date      DATE        NOT NULL,
  PRIMARY KEY (employee_id)
);

CREATE OR REPLACE TABLE Payoffs
(
  payment_id  INT      NOT NULL,
  employee_id SMALLINT NOT NULL,
  PRIMARY KEY (payment_id)
);