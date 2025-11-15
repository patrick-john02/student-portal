<script setup lang="ts">
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbSeparator,
  BreadcrumbPage,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"

import {
  Bell,
  Award,
  Trophy,
  Medal,
  Star,
  Crown,
  Target,
  Calendar,
  Download,
  Share2,
} from "lucide-vue-next"

const userRole = "Student"

// Academic Honors
const academicHonors = [
  {
    id: 1,
    title: "High Honors",
    description: "General Average of 95% or higher",
    quarter: "Quarter 2, 2024-2025",
    date: "December 2024",
    icon: Crown,
    color: "gold",
    grade: "95.5%",
  },
  {
    id: 2,
    title: "Honors",
    description: "General Average of 90% or higher",
    quarter: "Quarter 1, 2024-2025",
    date: "October 2024",
    icon: Award,
    color: "silver",
    grade: "92.3%",
  },
  {
    id: 3,
    title: "Perfect Attendance",
    description: "No absences for the entire quarter",
    quarter: "Quarter 2, 2024-2025",
    date: "December 2024",
    icon: Target,
    color: "blue",
    grade: "100%",
  },
]

// Subject Excellence Awards
const subjectAwards = [
  {
    id: 1,
    subject: "Mathematics",
    award: "Top Performer",
    description: "Highest grade in Mathematics",
    grade: "98%",
    quarter: "Quarter 2",
    icon: Trophy,
    color: "blue",
  },
  {
    id: 2,
    subject: "Science",
    award: "Excellence Award",
    description: "Outstanding performance in Science",
    grade: "96%",
    quarter: "Quarter 2",
    icon: Medal,
    color: "green",
  },
  {
    id: 3,
    subject: "English",
    award: "Most Improved",
    description: "Significant improvement from previous quarter",
    grade: "94%",
    quarter: "Quarter 2",
    icon: Star,
    color: "purple",
  },
]

// Recognition & Achievements
const achievements = [
  {
    id: 1,
    title: "Science Fair Champion",
    category: "Competition",
    description: "1st Place in Regional Science Fair",
    date: "January 2025",
    level: "Regional",
  },
  {
    id: 2,
    title: "Math Olympiad Qualifier",
    category: "Competition",
    description: "Qualified for National Math Olympiad",
    date: "November 2024",
    level: "National",
  },
  {
    id: 3,
    title: "Student Leader",
    category: "Leadership",
    description: "Class President - STEM Section A",
    date: "School Year 2024-2025",
    level: "School",
  },
  {
    id: 4,
    title: "Volunteer Service Award",
    category: "Community",
    description: "100+ hours of community service",
    date: "December 2024",
    level: "School",
  },
]

const getIconColor = (color: string) => {
  const colors: Record<string, string> = {
    gold: "text-yellow-600 bg-yellow-50",
    silver: "text-gray-600 bg-gray-50",
    blue: "text-blue-600 bg-blue-50",
    green: "text-green-600 bg-green-50",
    purple: "text-purple-600 bg-purple-50",
  }
  return colors[color] || "text-gray-600 bg-gray-50"
}

const getLevelBadge = (level: string) => {
  const levels: Record<string, any> = {
    Regional: { variant: "default", class: "bg-blue-500" },
    National: { variant: "default", class: "bg-green-500" },
    School: { variant: "secondary", class: "" },
  }
  return levels[level] || levels.School
}
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- HEADER -->
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 
               transition-[width,height] ease-linear"
      >
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem class="hidden md:block">
              <BreadcrumbLink href="/student/dashboard">
                Student
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator class="hidden md:block" />
            <BreadcrumbItem>
              <BreadcrumbPage>Honors & Awards</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>

        <div class="ml-auto flex items-center gap-2 px-4">
          <Button variant="outline" size="sm">
            <Bell class="h-4 w-4" />
          </Button>
        </div>
      </header>

      <!-- MAIN CONTENT -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Page Header -->
        <div class="rounded-lg border bg-gradient-to-r from-yellow-50 via-amber-50 to-background p-6">
          <div
            class="flex flex-col md:flex-row md:items-center md:justify-between gap-4"
          >
            <div>
              <h2 class="text-3xl font-bold">Honors & Awards</h2>
              <p class="text-muted-foreground mt-2">
                Your achievements and recognitions
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Share2 class="mr-2 h-4 w-4" />
                Share
              </Button>
              <Button>
                <Download class="mr-2 h-4 w-4" />
                Download Certificate
              </Button>
            </div>
          </div>
        </div>

        <!-- Summary Stats -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Total Awards</CardTitle>
              <Trophy class="h-4 w-4 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">10</div>
              <p class="text-xs text-muted-foreground mt-1">
                All-time achievements
              </p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Academic Honors</CardTitle>
              <Award class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">3</div>
              <p class="text-xs text-muted-foreground mt-1">This school year</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Subject Awards</CardTitle>
              <Medal class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">3</div>
              <p class="text-xs text-muted-foreground mt-1">Excellence awards</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Competitions</CardTitle>
              <Star class="h-4 w-4 text-purple-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">4</div>
              <p class="text-xs text-muted-foreground mt-1">Recognitions</p>
            </CardContent>
          </Card>
        </div>

        <!-- Academic Honors -->
        <Card>
          <CardHeader>
            <CardTitle>Academic Honors</CardTitle>
            <CardDescription>
              Recognition for outstanding academic performance
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div class="space-y-4">
              <div
                v-for="honor in academicHonors"
                :key="honor.id"
                class="p-6 border rounded-lg hover:shadow-md transition-shadow"
              >
                <div class="flex items-start gap-4">
                  <div
                    :class="[
                      'p-4 rounded-lg',
                      getIconColor(honor.color),
                    ]"
                  >
                    <component :is="honor.icon" class="h-8 w-8" />
                  </div>

                  <div class="flex-1">
                    <div class="flex items-start justify-between gap-4">
                      <div>
                        <h3 class="text-xl font-bold">{{ honor.title }}</h3>
                        <p class="text-muted-foreground mt-1">
                          {{ honor.description }}
                        </p>
                        <div class="flex items-center gap-3 mt-3">
                          <Badge variant="outline">{{ honor.quarter }}</Badge>
                          <span class="text-sm text-muted-foreground flex items-center gap-1">
                            <Calendar class="h-3 w-3" />
                            {{ honor.date }}
                          </span>
                        </div>
                      </div>
                      <div class="text-right">
                        <div class="text-2xl font-bold text-primary">
                          {{ honor.grade }}
                        </div>
                        <div class="text-xs text-muted-foreground">Grade</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Subject Excellence Awards -->
        <Card>
          <CardHeader>
            <CardTitle>Subject Excellence Awards</CardTitle>
            <CardDescription>
              Outstanding performance in individual subjects
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              <div
                v-for="award in subjectAwards"
                :key="award.id"
                class="p-4 border rounded-lg hover:shadow-md transition-shadow"
              >
                <div
                  :class="['p-3 rounded-lg inline-flex mb-3', getIconColor(award.color)]"
                >
                  <component :is="award.icon" class="h-6 w-6" />
                </div>
                <h3 class="font-bold text-lg">{{ award.subject }}</h3>
                <p class="text-sm font-semibold text-primary mt-1">
                  {{ award.award }}
                </p>
                <p class="text-sm text-muted-foreground mt-2">
                  {{ award.description }}
                </p>
                <div class="flex items-center justify-between mt-4">
                  <Badge variant="outline">{{ award.quarter }}</Badge>
                  <span class="font-semibold text-lg text-green-600">
                    {{ award.grade }}
                  </span>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Other Achievements -->
        <Card>
          <CardHeader>
            <CardTitle>Recognition & Achievements</CardTitle>
            <CardDescription>
              Competition wins, leadership roles, and community service
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div class="space-y-3">
              <div
                v-for="achievement in achievements"
                :key="achievement.id"
                class="p-4 border rounded-lg hover:shadow-md transition-shadow"
              >
                <div class="flex items-start justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex items-center gap-2 mb-2">
                      <h3 class="font-bold text-lg">{{ achievement.title }}</h3>
                      <Badge :variant="getLevelBadge(achievement.level).variant">
                        {{ achievement.level }}
                      </Badge>
                    </div>
                    <p class="text-sm text-muted-foreground">
                      {{ achievement.description }}
                    </p>
                    <div class="flex items-center gap-3 mt-3">
                      <Badge variant="outline">{{ achievement.category }}</Badge>
                      <span class="text-xs text-muted-foreground flex items-center gap-1">
                        <Calendar class="h-3 w-3" />
                        {{ achievement.date }}
                      </span>
                    </div>
                  </div>
                  <Trophy class="h-8 w-8 text-yellow-600" />
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Call to Action -->
        <Card class="bg-gradient-to-r from-blue-50 to-purple-50 border-2 border-blue-200">
          <CardContent class="p-6">
            <div class="flex items-center justify-between gap-4">
              <div class="flex items-center gap-4">
                <div class="h-12 w-12 bg-blue-500 rounded-full flex items-center justify-center">
                  <Star class="h-6 w-6 text-white" />
                </div>
                <div>
                  <h3 class="font-bold text-lg">Keep Up the Great Work!</h3>
                  <p class="text-sm text-muted-foreground">
                    You're on track to achieve more honors this quarter.
                  </p>
                </div>
              </div>
              <Button>View Progress</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>