<script lang="ts">
export const description = "Teacher grade overview page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

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
  BreadcrumbPage,
  BreadcrumbSeparator,
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
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import { BarChart3, MoreHorizontal, BookOpen, Users, ArrowRight } from "lucide-vue-next"

const userRole = "Teacher"

// Dummy subjects & grade overview
const subjects = ref([
  {
    id: 1,
    subject: "General Mathematics",
    section: "STEM 11 - A",
    gradeLevel: "Grade 11",
    students: 45,
    avg: 87.4,
    color: "bg-blue-500",
  },
  {
    id: 2,
    subject: "Oral Communication",
    section: "HUMSS 11 - B",
    gradeLevel: "Grade 11",
    students: 38,
    avg: 90.2,
    color: "bg-green-500",
  },
  {
    id: 3,
    subject: "Practical Research 2",
    section: "ABM 12 - A",
    gradeLevel: "Grade 12",
    students: 42,
    avg: 85.1,
    color: "bg-yellow-500",
  },
  {
    id: 4,
    subject: "Physical Education 2",
    section: "GAS 12 - C",
    gradeLevel: "Grade 12",
    students: 40,
    avg: 92.3,
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Page Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Grades</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Grades Overview</h2>
            <p class="text-sm text-muted-foreground">
              View, manage, and analyze grades for your subjects.
            </p>
          </div>
        </div>

        <!-- Search -->
        <div class="flex items-center justify-between">
          <Input
            v-model="search"
            placeholder="Search subject..."
            class="max-w-xs"
          />
        </div>

        <!-- Subjects Table -->
        <Card>
          <CardHeader>
            <CardTitle>Your Subjects</CardTitle>
            <CardDescription>
              Select a subject to view or input grades.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">Subject</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead class="text-center w-28">Students</TableHead>
                  <TableHead class="text-center w-28">Average</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="sub in subjects"
                  :key="sub.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div class="h-3 w-3 rounded-full" :class="sub.color"></div>
                      <p class="font-medium">{{ sub.subject }}</p>
                    </div>
                  </TableCell>

                  <TableCell>{{ sub.section }}</TableCell>

                  <TableCell>
                    <Badge variant="secondary">
                      {{ sub.gradeLevel }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-center">
                    <Badge variant="outline">
                      <Users class="h-3 w-3 mr-1" />
                      {{ sub.students }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-center font-semibold">
                    {{ sub.avg }}%
                  </TableCell>

                  <TableCell class="text-right">
                    <Button variant="ghost" size="icon">
                      <ArrowRight class="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

        <!-- Summary Stats -->
        <div class="grid gap-4 md:grid-cols-3">
          <Card>
            <CardHeader>
              <CardTitle class="text-base">Highest Subject Average</CardTitle>
            </CardHeader>
            <CardContent>
              <p class="text-3xl font-bold text-green-600">92.3%</p>
              <p class="text-sm text-muted-foreground mt-1">Physical Education 2</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle class="text-base">Lowest Subject Average</CardTitle>
            </CardHeader>
            <CardContent>
              <p class="text-3xl font-bold text-red-600">85.1%</p>
              <p class="text-sm text-muted-foreground mt-1">Practical Research 2</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle class="text-base">Overall Performance</CardTitle>
            </CardHeader>
            <CardContent>
              <p class="text-3xl font-bold text-primary">88.7%</p>
              <p class="text-sm text-muted-foreground mt-1">Across all subjects</p>
            </CardContent>
          </Card>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
