FactoryBot.define do
  factory :location do
    name { "Sevananda Natural Foods" }
    address { "467 Moreland Ave NE, Atlanta, GA, 30307" }
    latitude { 33.7627 }
    longitude { -84.3496 }
    ebt { true }
    source { "GA-EBT.csv" }

    trait :ungeocoded do
      latitude { nil }
      longitude { nil }
    end
  end
end
