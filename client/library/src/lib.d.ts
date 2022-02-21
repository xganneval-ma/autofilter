abstract interface BaseOperator {
  field: string;
  value: string | number | boolean;
}

interface OperatorEq extends BaseOperator {
  type: "Eq";
}

interface OperatorLt extends BaseOperator {
  type: "Lt";
}

interface OperatorLte extends BaseOperator {
  type: "Lte";
}

interface OperatorGt extends BaseOperator {
  type: "Gt";
}

interface OperatorGte extends BaseOperator {
  type: "Gte";
}

interface OperatorLike extends BaseOperator {
  type: "Like";
}

type Operator =
  | OperatorEq
  | OperatorLt
  | OperatorLte
  | OperatorGt
  | OperatorGte
  | OperatorLike;

interface ExpressionNot {
  type: "Not";
  operator: Operator;
}

interface ExpressionLink {
  type: "And" | "Or";
  children: (Operator | ExpressionNot | ExpressionLink)[];
}

type Expression = ExpressionNot | ExpressionLink;

type Criterion = Operator | Expression;
